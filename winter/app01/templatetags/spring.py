#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def my_define_func(a, b):
    return a + b
