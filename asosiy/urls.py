

from django.urls import path
from .views import *

from .views import BolimlarView

urlpatterns = [

    path('', BolimlarView.as_view()),
    path('maxsulotlar/', MaxsulotlarView.as_view()),

]
