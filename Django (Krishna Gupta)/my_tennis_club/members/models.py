from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    address = models.TextField(max_length=255,null=True)
    joined_date = models.DateField(null=True)
