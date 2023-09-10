from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')

def say_search(request):
    return render(request,'a.html',{'name':'NAGARAJU'})

def home(request):
    peoples=[
        {'name':'Nagaraju','age':'24'},
        {'name':'raju','age':'25'},
        {'name':'Nagar','age':'26'},
        {'name':'king','age':'27'},
        {'name':'lord','age':'28'},
    ]
    return render(request,'b.html',context={'peoples':peoples})
def navbar(request):
    peoples=[
        {'name':'Nagaraju','age':'24'},
        {'name':'raju','age':'25'},
        {'name':'Nagar','age':'26'},
        {'name':'king','age':'27'},
        {'name':'lord','age':'28'},
    ]
    return render(request,'navbar.html',context={'peoples':peoples})
    