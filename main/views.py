from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Notice


def index(request):
    print(request)
    print(type(request))
    print(dir(request))
    print('-----------')
    print(request.POST)
    return render(request, 'index.html')

def test(request):
    d={'name':'chanyong' ,'age':24}
    return JsonResponse(d)
    

def sample(request):
    d= Notice.objects.all()
    #d={'name':'hojun','age':10}
    #l=[100,200,300]
    return render(request,'sample.html',{'value':d})