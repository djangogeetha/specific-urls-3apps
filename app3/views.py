from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nine(request):
    return HttpResponse('bakkaaa......')

def seven(request):
    return render(request,'seven.html')


def eight(request):
    return render(request,'eight.html')

