from django.urls import path
from . import views
from vege import *

urlpatterns = [
    path('receipes/',views.receipes, name='receipes')
    
]
