"""autumn URL Configuration

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
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^set_business/', views.set_business),
    url(r'^get_business$', views.get_business),
    url(r'^set_host$', views.set_host),
    url(r'^get_host$', views.get_host),
    url(r'^test_ajax$', views.test_ajax),
    url(r'^set_app$', views.set_app),
    url(r'^app$', views.app),
    url(r'^ajax_add_app$', views.ajax_add_app),
    url(r'^ajax_edit_app$', views.ajax_edit_app),
    url(r'^ajax_del_app$', views.ajax_del_app),
]

