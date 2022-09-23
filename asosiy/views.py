from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Omborxona


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')
class MaxsulotlarView(View):
    def get(self, request):
        ombor=Omborxona.objects.get(user=request.user)
        data={
            "mahsulotlar":Maxsulot.objects.filter(ombor=ombor)
        }
        return render(request, 'products.html', data)
    def post(self,request):
        Maxsulot.objects.create(
            nom=request.POST.get("n"),
            brend=request.POST.get("b"),
            narx=request.POST.get("m_n"),
            miqdor=request.POST.get("m"),
            olchov=request.POST.get("m_o"),
            ombor=Omborxona.objects.get(user=request.user)
        )
        return redirect("/bolimlar/mahsulotlar/")

class ClientView(View):
    def get(self,request):
        ombor = Omborxona.objects.get(user=request.user)
        data={
            "clientlar":Client.objects.filter(ombor=ombor)
        }
        return render(request, "clients.html", data)

    def post(self, request):
        Client.objects.create(
            ism=request.POST.get("i"),
            nom=request.POST.get("n"),
            tel=request.POST.get("t"),
            manzil=request.POST.get("m"),
            qarz=request.POST.get("q"),
            ombor=Omborxona.objects.get(user=request.user)
        )
        return redirect("/bolimlar/clientlar/")





