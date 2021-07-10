from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import index, test, sample
from a.views import indexA
from b.views import indexB, indexBdetail
from c.views import indexC
from d.views import indexD


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('sample/',sample),
    path('testtest/',test),
    path('aa/',include('a.urls')),
    path('bb/',indexB),
    path('bb/<int:pk>/',indexBdetail),
    path('cc/',indexC),
    path('dd/',indexD),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)