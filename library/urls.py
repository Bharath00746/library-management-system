"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libapp import views as lib_app

from django.conf.urls.static import static
from library import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lib_app.login, name='login'),
    path('signup',lib_app.signup,name='signup'),
    path('bookdetails',lib_app.bookdetails,name='bookdetails'),
    path('bookadmin',lib_app.bookdmin, name='bookadmin'),
    path('updatebook/(?P<pk>/$',lib_app.updatebook,name='updatebook'),
    path('deletebook/(?P<pk>/$',lib_app.deletebook,name='deletebook'),
    # path('bookstatus',lib_app.bookstatus, name='availablebook'),
    # path('deletebook/(?P<pk>/$',lib_app.deletebook,name='deletebook'),
    path('bookshow', lib_app.bookshow, name='bookshow'),
    path('takebook/(?P<pk>/$',lib_app.takebook,name='takebook'),
    path('returnbook/(?P<pk>/$',lib_app.returnbook,name='returnbook'),
    path('restapi',lib_app.restapidemo,name="restapi")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
