from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import index, test, sample
from a.views import indexA
from b.views import indexB, indexBdetail
# from c.views import indexC
from c.views import BlogList,BlogDetail
from d.views import indexD, testview,SignupView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('sample/',sample),
    path('testtest/',test),
    path('aa/',include('a.urls')),
    path('bb/',indexB),
    path('bb/<int:pk>/',indexBdetail),
    path('cc/',BlogList.as_view()),
    path('cc/<int:pk>/',BlogDetail.as_view()),
    path('dd/',indexD),
    path('dd/test/',testview),
    path('dd/signup/',SignupView.as_view()),
    path('dd/login/',LoginView.as_view()),
    path('dd/logout/',LogoutView.as_view()),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)