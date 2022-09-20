
from django.contrib import admin
from django.urls import path, include
from userapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view()),
    path('bolimlar/', include('asosiy.urls')),
]
