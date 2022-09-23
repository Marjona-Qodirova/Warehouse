from django.db import models
from userapp.models import *




class Maxsulot(models.Model):
    nom=models.CharField(max_length=50)
    narx=models.IntegerField()
    brend=models.CharField(max_length=30)
    miqdor=models.PositiveSmallIntegerField()
    olchov=models.CharField(max_length=12, choices=[("kg","kg"), ("dona","dona"),("qop","qop")])
    kelgan_sana=models.DateTimeField(auto_now_add=True)
    ombor=models.ForeignKey(Omborxona, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Client(models.Model):
    ism=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)
    tel=models.CharField(max_length=20)
    qarz=models.IntegerField(default=0)
    manzil=models.CharField(max_length=30)
    ombor = models.ForeignKey(Omborxona, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


