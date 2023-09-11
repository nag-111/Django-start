from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .models import Personal_Details

# Create your views here.
def wel_come(request):
    return HttpResponse('Hello world')

def page_login(request):
    return render(request,'page1.html',{'name':'nagaraj k'})

def data_move(request):
    data_from_db = Blog.objects.all
    return render(request, 'page1.html',{'getdata':data_from_db})

def info(request):
    details = Personal_Details.objects.all()
    return render(request, 'page2.html',{'info':details})