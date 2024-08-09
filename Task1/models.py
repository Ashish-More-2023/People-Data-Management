from django.db import models


class Profiles(models.Model):
 name = models.CharField(max_length=100)
 username = models.CharField(max_length=100)
 email = models.EmailField()
 id = models.AutoField(primary_key=True)

# Create your models here.