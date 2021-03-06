"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from . import views
from guestbook.views import guestbook_list
from helloworld.views import login,logout
#from helloworld.views import register
from helloworld.views import signup,personalpage
#from helloworld.views import login
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guestbook/', views.index),
    path('signup/', views.signup),
    path('', guestbook_list),
    path('login/', views.login),
    path('logout/', views.logout),
    path('personalpage/', views.personalpage),


]
