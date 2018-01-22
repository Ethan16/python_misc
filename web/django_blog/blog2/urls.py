# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-20 09:05:51
@Author  : Ethan (euler52201044@163.com)
@Link    : https://github.com/Ethan16
@file    : urls.py
@usage   : 
@Version : 1.0
@Change  : 2018-01-20 09:05:51
"""


from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index/$', views.index),
]
