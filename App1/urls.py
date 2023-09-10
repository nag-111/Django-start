from django.urls import path
from . import views

urlpatterns =[
    path('welcome/',views.wel_come),
    path('login/',views.page_login),
]