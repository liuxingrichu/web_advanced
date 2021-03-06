"""winter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, {'name': 'Lucy'}),
    url(r'^a/', include('app01.urls', namespace='m1')),
    url(r'^b/', include('app01.urls', namespace='m2')),
    url(r'^submaster$', views.submaster),
    url(r'^submaster1$', views.submaster1),
    url(r'^simple$', views.simple),
    # url(r'^page-(\d+).html', views.page),
    url(r'^page', views.page),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
]
