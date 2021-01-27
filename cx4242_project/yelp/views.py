# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("project_visualization.html")
    return HttpResponse(template.render({'var1': "hello world!"}))
# Create your views here.
