# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('Hello world!')
    # http://127.0.0.1:8000/blog/index/
    return render(request, 'blog/index.html', {'hello': 'Hello,James!'})
