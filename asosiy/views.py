from django.shortcuts import render
from django.views import View


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')
class MaxsulotlarView(View):
    def get(self, request):
        return render(request, 'products.html')



