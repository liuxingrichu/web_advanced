#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server


def handle_index():
    with open('index.html', 'rb') as f:
        data = f.read()
    return [data, ]


def handle_date():
    return ["<h1>Hello, date!</h1>".encode("utf-8"), ]


URL_DICT = {
    "/index": handle_index,
    "/date": handle_date,
}


def RunServer(environ, start_response):
    """
    :param environ:客户发来的所有数据
    :param start_response:封装要返回给用户的数据，响应头状态
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url = environ["PATH_INFO"]
    func = None
    if current_url in URL_DICT:
        func = URL_DICT.get(current_url)
    if func:
        return func()
    else:
        return "<h1>404</h1>".encode("utf-8")


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
