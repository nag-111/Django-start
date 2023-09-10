from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wel_come(request):
    return HttpResponse('Hello world')

def page_login(request):
    return render(request,'page1.html',{'name':'nagaraj k'})