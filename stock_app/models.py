from django.db import models

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     F_name= models.CharField(max_length=255)
     L_name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "Message from " + self.F_name + ' - ' + self.email
