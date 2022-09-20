from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View



class  LoginView(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        user = authenticate(username=request.POST.get("login"), password=request.POST.get("password"))
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect("/bolimlar/")

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/bolimlar/')





