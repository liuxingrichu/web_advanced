#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
import inspect


class Row1(MiddlewareMixin):
    def process_request(self, request):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))

    def process_view(self, request, view_func, view_func_args,
                     view_func_kwargs):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))

    def process_response(self, request, response):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response

    def process_exception(self, request, exception):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        if isinstance(exception, ValueError):
            return HttpResponse('%s出现异常' % self.__class__.__name__)

    def process_template_response(self, request, response):
        # 如果Views中的函数返回的对象中，具有render方法
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response


from django.shortcuts import HttpResponse


class Row2(MiddlewareMixin):
    def process_request(self, request):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        # return HttpResponse('go out')

    def process_view(self, request, view_func, view_func_args,
                     view_func_kwargs):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))

    def process_response(self, request, response):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response

    def process_exception(self, request, exception):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        if isinstance(exception, ValueError):
            return HttpResponse('%s出现异常' % self.__class__.__name__)

    def process_template_response(self, request, response):
        # 如果Views中的函数返回的对象中，具有render方法
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response


class Row3(MiddlewareMixin):
    def process_request(self, request):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))

    def process_view(self, request, view_func, view_func_args,
                     view_func_kwargs):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))

    def process_response(self, request, response):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response

    def process_exception(self, request, exception):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        if isinstance(exception, ValueError):
            return HttpResponse('%s出现异常' % self.__class__.__name__)

    def process_template_response(self, request, response):
        # 如果Views中的函数返回的对象中，具有render方法
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return response
