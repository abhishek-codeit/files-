from django.db import models


# Create your models here.
class Contact(models.Model):
       name = models.CharField(max_length=100)
       year = models.CharField(max_length=100)
       email = models.TextField()
       branch = models.TextField()
       usn = models.CharField(max_length=10)






