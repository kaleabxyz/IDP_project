from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=100, null= True)
    last_name = models.CharField(max_length=100, null=True)
    speciality = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    biography = models.TextField(null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField() 
    date_of_appointment = models.DateField()
    accountnumber = models.CharField(max_length=50)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    bank = models.CharField(max_length=30, null=True)
    

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"




class Room(models.Model):
    roomnumber = models.CharField(max_length=30)
    availability = models.BooleanField()

    def __str__(self) -> str:
        return self.roomnumber


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
  
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    admission = models.DateField()
    age =models.IntegerField(null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    notes = models.TextField(null=True)
    bloodtype = models.CharField(max_length=3)
    weight = models.CharField(max_length=5)
    height = models.FloatField(max_length=4) 
    doctor_first_name = models.CharField(max_length=200, null=True)
    doctor_last_name = models.CharField(max_length=200, null=True)
    roomnumber = models.CharField(max_length=30, null=True)
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null = True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)


     
    



