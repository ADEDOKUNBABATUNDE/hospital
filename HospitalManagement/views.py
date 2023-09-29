from django.shortcuts import render,redirect ,reverse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout ,login
from django.contrib import messages
from django.contrib import messages, auth
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context={

    }
    return render(request,"Hospitalmanagement/index.html",context)

def Login(request):
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        # if  request.user.is_staff:
        if user is not None and user.is_staff:
            auth.login(request, user)
            messages.success(request, "you have successfully login")
            return redirect('admin_dashboard')

        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')
    return render(request, 'HospitalManagement/login.html')


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    messages.success(request, "you have successfully loggedout")
    return redirect(home)


def admin_dashboard(request):
    doctors=Doctor.objects.all().order_by('-id')
    patients=Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=Doctor.objects.all().filter(status=False).count()

    patientcount=Patient.objects.all().filter(status=True).count()
    pendingpatientcount=Patient.objects.all().filter(status=False).count()

    appointmentcount=Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=Appointment.objects.all().filter(status=False).count()
    context={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,"HospitalManagement/admin_dashboard.html",context)

def admin_patient(request):
    context={

    }
    return render(request,"HospitalManagement/admin_patient.html",context)

def admin_doctor(request):
    context={

    }
    return render(request,"HospitalManagement/admin_doctor.html",context)

def admin_appointment(request):
    context={

    }
    return render(request,"HospitalManagement/admin_appointment.html",context)

def admin_view_doctor(request):
    doctors=Doctor.objects.all().order_by('-id')
    context={
    'doctors': doctors,
    
    }
    return render(request,"HospitalManagement/admin_view_doctor.html",context)



def admin_add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_doctor')
    else:
        form = DoctorForm() 
    context={
         'form': form,

    }
    return render(request,"HospitalManagement/admin_add_doctor.html",context)

# approve and reject for admin doctor
def approve_doctor(request,pk):
    doctor=Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin_dashboard'))


def reject_doctor(request,pk):
    doctor=Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('admin_dashboard')

def admin_approve_doctor(request):
    doctors=Doctor.objects.all().order_by('-id')
    context={
    'doctors': doctors,
    
    }
    return render(request,"HospitalManagement/admin_approve_doctor.html",context)

# approve and reject for admin patient
def approve_patient(request,pk):
    patient=Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('admin_dashboard'))


def reject_patient(request,pk):
    patient=Patient.objects.get(id=pk)
    patient.delete()
    return redirect('admin_dashboard')

def admin_approve_patient(request):
    patients=Patient.objects.all()
    context={
    'patients': patients,
    
    }
    return render(request,"HospitalManagement/admin_approve_patient.html",context)

# approve and reject for appointment
def approve_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('admin_dashboard'))


def reject_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('admin_dashboard')

def admin_approve_appointment(request):
    appointments=Appointment.objects.all()
    context={
    'appointments': appointments,
    
    }
    return render(request,"HospitalManagement/admin_approve_appointment.html",context)



def admin_view_appointment(request):
    appointments=Appointment.objects.all().order_by('-id')
    context={
    'appointments': appointments,
    
    }
    return render(request,"HospitalManagement/admin_view_appointment.html",context)

def admin_book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_appointment')
    else:
        form = AppointmentForm() 
    context={
         'form': form,

    }
    return render(request,"HospitalManagement/admin_book_appointment.html",context)




def admin_view_patient(request):
    patients=Patient.objects.all().order_by('-id')
    context={
    'patients':patients,
    
    }
    return render(request,"HospitalManagement/admin_view_patient.html",context)


def doctor_specialization(request):
    doctors=Doctor.objects.all().filter(status=True)
    context={
        'doctors':doctors,
    }
    return render(request,'HospitalManagement/doctor_specialization.html',context)

def admit_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_patient')
    else:
        form = PatientForm() 
    context={
         'form': form,

    }
    return render(request,"HospitalManagement/admit_patient.html",context)




#================================================= patient dashboard views start ==============================================
def patient_dashboard(request):
    context={
      
    }
    return render(request,'HospitalManagement/patient_dashboard.html',context)



def patientlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            messages.success(request, "you have successfully login")
            return redirect('patient_dashboard')

        else:
            messages.error(request, "Invalid username or password")
            return redirect('patientlogin')
    return render(request, 'HospitalManagement/patientlogin.html')




def patientsignup(request):
    if request.method =="POST":
        form =PatientsignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , ' successfully registered ')
            return redirect('patientlogin')
    else:
         form = PatientsignupForm()
    context = {
        'form':form,
    }          
        
    return render(request, 'HospitalManagement/patientsignup.html',context)    









# =========================doctor view start========================================
def doctor_dashboard(request):
    context={
      
    }
    return render(request,'HospitalManagement/doctor_dashboard.html',context)






def doctorsignup(request):
    if request.method =="POST":
        form =DoctorsignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , ' successfully registered ')
            return redirect('doctorlogin')
    else:
         form = DoctorsignupForm()
    context = {
        'form':form,
    }          
        
    return render(request, 'HospitalManagement/doctorsignup.html',context)    




def doctorlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            messages.success(request, "you have successfully login")
            return redirect('doctor_dashboard')

        else:
            messages.error(request, "Invalid username or password")
            return redirect('doctorlogin')
    return render(request, 'HospitalManagement/doctorlogin.html')


def doctor_patient(request):
    context = {
        
    }          
        
    return render(request, 'HospitalManagement/doctor_patient.html',context)    


def doctor_appointment(request):
    context = {
        
    }          
        
    return render(request, 'HospitalManagement/doctor_appointment.html',context) 


def doctor_dashboard_view(request):
    #for three cards
    patientcount=Patient.objects.all().filter(status=True).count()
    appointmentcount=Appointment.objects.all().filter(status=True).count()
   
    #for  table in doctor dashboard
    appointments=Appointment.objects.all().filter(status=True).order_by('-id')
    patient=[]
    for a in appointments:
        patient.append(a.patient)
    patients=Patient.objects.all().filter(status=True).order_by('-id')
    appointments=zip(appointments,patients)
    context={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'appointments':appointments,
    
    }
    return render(request,'HospitalManagement/doctor_dashboard.html',context)    

def patient_dashboard_view(request):
    # patients=Patient.objects.get(address=Doctor.name)

    context={
    # 'patients':patients,
    # 'doctorName':doctor.name,
    # 'doctorMobile':doctor.mobile,
    # 'doctorAddress':doctor.address,
    # 'symptoms':patients.symptoms,
    # 'doctorDepartment':doctor.specialization,
    # 'doctorgender':patients.gender,
    
    }
    return render(request,'HospitalManagement/patient_dashboard.html',context)

def patient_appointment(request):
    context={
   
    
    }
    return render(request,'HospitalManagement/patient_appointment.html',context)

def patient_view_appointment(request):
    appointments=Appointment.objects.all().filter(patient=request.user.id)
    return render(request,'HospitalManagement/patient_view_appointment.html',{'appointments':appointments})
   

def patient_book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_appointment')
    else:
        form = AppointmentForm() 
    context={
         'form': form,

    }
    return render(request,"HospitalManagement/patient_book_appointment.html",context)


def doctor_view_patient(request):
    patients=Patient.objects.all().filter(status=True)
    # doctor=Doctor.objects.get() #for profile picture of doctor in sidebar
    return render(request,'HospitalManagement/doctor_view_patient.html',{'patients':patients})
def admin_update(request,pk):
    patient = get_object_or_404(Patient , id=pk)
   
    form =PatientForm(request.POST or None , instance=patient)
    if form.is_valid():
        form.save()
        patient_Title = f'You have successfully updated {patient.name}'
        messages.success(request,patient_Title)
        return redirect('admin_view_patient')
    return render (request,'HospitalManagement/admin_update.html',{'form':form})
def admin_delete(request,pk):
    patient = get_object_or_404(Patient, id=pk)
    patient.delete()
    patient_Title = f'You have successfully deleted{patient.name}'
    messages.error(request,patient_Title)
    return redirect('admin_patient')




def admin_update_d(request,pk):
    doctor = get_object_or_404(Doctor , id=pk)
    form =DoctorForm(request.POST or None , instance=doctor)
    if form.is_valid():
        form.save()
        patient_Title = f'You have successfully updated {doctor.name}'
        messages.success(request,patient_Title)
        return redirect('admin_view_doctor')
    return render (request,'HospitalManagement/admin_update_d.html',{'form':form})
def admin_delete_d(request,pk):
    doctor = get_object_or_404(doctor, id=pk)
    doctor.delete()
    patient_Title = f'You have successfully deleted{doctor.name}'
    messages.error(request,patient_Title)
    return redirect('admin_doctor')


def doctor_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_patient')
    else:
        form = PatientForm() 
    context={
         'form': form,

    }
    return render(request,"HospitalManagement/doctor_add.html",context)
