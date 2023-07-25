from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def third(request):
    return HttpResponse('VDJCDIJDKCHDIJCDCDC')

def first(request):
    return render(request,'first.html')


def second(request):
    return render(request,'second.html')
