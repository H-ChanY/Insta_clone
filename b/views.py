from django.shortcuts import render
from .models import Blog

def indexB(request):
    context= Blog.objects.all()
    return render(request, 'indexB.html', {'context':context})
    
def indexBdetail(request,pk):
    blog= Blog.objects.get(pk=pk)
    context={
        'blog':blog,
    }
    return render(request, 'indexBdetail.html',context)
