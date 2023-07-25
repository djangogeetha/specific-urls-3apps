from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def six(request):
    return HttpResponse('geetha......')

def four(request):
    return render(request,'four.html')


def five(request):
    return render(request,'five.html')
