from django.contrib import admin
from django.urls import path
from main.views import index, test, sample
from a.views import indexA
from b.views import indexB
from c.views import indexC
from d.views import indexD


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('sample/',sample),
    path('testtest/',test),
    path('aa/',indexA),
    path('bb/',indexB),
    path('cc/',indexC),
    path('dd/',indexD),
]
