from django.db import models

# Create your models here.

# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
  

class Membernew(models.Model):
  def __str__(self) -> str:
    return self.firstname

  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  rollno = models.IntegerField(null=True)
  phoneno =models.IntegerField(null=True)
  image = models.ImageField(default='default.jpg',upload_to='member_photo/')


 

