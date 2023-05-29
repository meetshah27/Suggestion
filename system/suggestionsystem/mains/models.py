from django.db import models

# Create your models here.
class Login(models.Model):
    Mail = models.CharField(primary_key=True, max_length=50, default=None)
    Role = models.CharField(max_length=50, default=None)
    Department = models.CharField(max_length=50, default=None)

    def __str__(self):  
        return self.Mail
class Suggestion_Data(models.Model):
    Form_id=models.AutoField(primary_key=True)
    Mail = models.CharField(max_length=50, default=None)
    Title= models.CharField(max_length=50, default=None)
    Description= models.CharField(max_length=250, default=None, null=True)
    Attachment=models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
    Status_A=models.CharField(max_length=20, default="Pending")
    Manager_mail=models.CharField(max_length=50,default=None, null=True)
    Status_M= models.CharField(max_length=20, default="Pending")
    Answer= models.CharField(max_length=350, default=None, null=True)
    Entry_Time=models.TimeField(auto_now_add=True)

def __str__(self):  
    return  self.Form_id

