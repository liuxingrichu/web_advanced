#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server


def handle_index():
    return [bytes('<h1>Hello, index!</h1>', encoding='utf-8'), ]


def handle_date():
    return ["<h1>Hello, date!</h1>".encode("utf-8"), ]


def RunServer(environ, start_response):
    """
    :param environ:客户发来的所有数据
    :param start_response:封装要返回给用户的数据，响应头状态
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url = environ["PATH_INFO"]
    if current_url == "/index":
        return handle_index()
    elif current_url == "/date":
        return handle_date()
    else:
        return "<h1>404</h1>".encode("utf-8")


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
