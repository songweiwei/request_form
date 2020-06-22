# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/6/22 16:48
import os, re, json, traceback
import requests
import request
from flask import make_response

def get(url):
    '''
    get请求，传入网址
    :param url: 请求的网址
    :return:
    '''
    http=requests.get(url)
    http.encoding="utf-8"
    print("http为：%s" %http)
    print("http.status_code为：%d" % http.status_code)
    print("http.encoding为：%s" % http.encoding)
    print("http.text为：%s" % http.text)
    return http.text


def post(url,data):
    data={"k1":"value1"}
    data_json=json.dumps(data,ensure_ascii=False)
    http_post=requests.post(url,data=data_json.encode("utf-8"))
    print("http_post为：%s" %http_post)
    print("http_post.status_code为：%d" % http_post.status_code)
    print("http_post.encoding为：%s" % http_post.encoding)
    print("http_post.text为：%s" % http_post.text)
    return http_post




def get_data_param():
    '''
    获取请求的参数
    :return: get_data获取未经处理的原始数据，如果是json，则返回json，有序
    '''
    return request.get_data()


def get_json_param():
    '''
    获取请求的参数
    :return: 将请求的参数进行处理，得到的是字典格式，无序
    '''
    return request.get_json()

def data_param():
    '''
    获取请求的参数
    :return: 获取未经处理的原始数据，如果是json，则返回json，有序
    '''
    return request.data

def json_parms():
    '''
    将请其参数做了处理，返回字典格式，无序
    :return:
    '''
    return request.json


def make_response_data(data):
    '''
    给数据增加application/json头
    :param data:字典数据dict
    :return: 返回带有json头的数据
    '''
    resp=make_response(data=data)
    resp.headers["Content-Type"]=r"application/json"
    return resp



if __name__ == '__main__':
    get("https://www.baidu.com/")






















































