from django.db import models
# Create your models here.


specialization=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile= models.IntegerField()
    address=models.CharField(max_length=200)
    specialization = models.CharField(max_length=50,choices=specialization,default='Cardiologist')
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    image= models.ImageField('profile' ,upload_to='images/',null=True,blank=True)
    gender= models.CharField(max_length=10)
    mobile= models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=100 ,null=True,blank=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE) 
    appointmentdate=models.DateField()
    appointmenttime=models.TimeField() 
    description=models.TextField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name