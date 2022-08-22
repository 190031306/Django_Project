from django.shortcuts import render
from django.http import HttpResponse

def demofunction(request):
    return HttpResponse("demo project")
def mainfunction(request):
    return render(request,"project.html")
