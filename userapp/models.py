from django.contrib.auth.models import User
from django.db import models




class Omborxona(models.Model):
    nom=models.CharField(max_length=50)
    manzil=models.CharField(max_length=50)
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    soha=models.CharField(max_length=30)
    def __str__(self):
        return self.nom

