#! /usr/bin/env python
#! coding:utf-8
__author__ = 'shine_forever'

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns('',
    url(r'^test/$', TemplateView.as_view(template_name='test.html')),
    url(r'^test123/$', TemplateView.as_view(template_name='test.jinja.html')),
    url(r'^update/$',Update_ServerList.as_view(),name='update_serverlist'),


)
