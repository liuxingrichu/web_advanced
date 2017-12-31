#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url

from app01 import views

# app_name = 'app01'
urlpatterns = [
    url(r'^home$', views.home, name='HOME')
]
