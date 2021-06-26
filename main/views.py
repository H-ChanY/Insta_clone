from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

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
    

