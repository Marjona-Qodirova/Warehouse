

from django.urls import path
from .views import *

from .views import BolimlarView

urlpatterns = [

    path('', BolimlarView.as_view()),
    path('mahsulotlar/', MaxsulotlarView.as_view()),
    path('clientlar/', ClientView.as_view()),

]
