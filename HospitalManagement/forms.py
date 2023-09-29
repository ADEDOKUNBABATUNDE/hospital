from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from typing import Any
from django.contrib.auth.models import User






class DoctorForm(ModelForm):

    class Meta():
        model=Doctor
        fields =("__all__")


   
    
class AppointmentForm(ModelForm):

    class Meta():
        model=Appointment
        fields =("__all__")  


class PatientForm(ModelForm):

    class Meta():
        model=Patient
        fields =("__all__")          

# ==========================patient signup=============================
class PatientsignupForm(UserCreationForm):
    email = forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
  
 


    class Meta():
        model = User
        fields = ('username','email','password1','password2')
     
    def __init__(self, *args: Any, **Kwargs: Any) -> None :
      super(PatientsignupForm,self).__init__(*args,**Kwargs)
      for fieldname in ('username','password1','email','password2'):
        self.fields[fieldname].help_text = None


#-=================== doctor sigup===========================================
class DoctorsignupForm(UserCreationForm):
    email = forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    

    class Meta():
        model = User
        fields = ('username','email','password1','password2')
     
    def __init__(self, *args: Any, **Kwargs: Any) -> None :
      super(DoctorsignupForm,self).__init__(*args,**Kwargs)
      for fieldname in ('username','password1','email','password2'):
        self.fields[fieldname].help_text = None



