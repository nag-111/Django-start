from django.urls import path
from . import views

urlpatterns =[
    path('hello/',views.say_hello),
    path('search/',views.say_search),
    path('home/',views.home),
    path('navbar/',views.navbar),
]