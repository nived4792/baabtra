from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'test.html')

def demo(request0):
    return HttpResponse("HELLO")

# Create your views here.
