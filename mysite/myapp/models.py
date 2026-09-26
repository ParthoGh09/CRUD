from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,blank=False)
    s_id=models.CharField(max_length=20,unique=True)
    dob=models.DateField()
    email=models.EmailField(max_length=50,unique=True)
    department=models.CharField(max_length=50,blank=False)

    def __str__(self):
         return self.s_id