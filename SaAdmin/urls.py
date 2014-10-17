#! /usr/bin/env python
#! coding:utf-8
__author__ = 'shine_forever'

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^test/$', TemplateView.as_view(template_name='test.html')),
    url(r'^test123/$', TemplateView.as_view(template_name='test.jinja.html')),
)
