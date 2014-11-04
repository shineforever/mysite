#! /usr/bin/env python
# coding:utf-8

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import View
import urllib2

# Create your views here.

def hello2(request):
    return render_to_response("hello.html")

def login(request):
    if request.method == 'GET':
        print request.GET
        return render_to_response("login.html")
#    user = request.GET["user"]
#    passwd = request.GET["passwd"]
#
#    if user == 'guolt' and passwd == '123':
#        return render_to_response("login.html")
#    else:
#        return render_to_response("login.html",{'err':"Login failure!!!"})
#

def hello(request):
    return HttpResponse('hello world!')


def current_url_view_good(request):
    """
    just test request!
    """
    return HttpResponse("Welcome to the page at %s" % request.path)


def get_host(request):
    return HttpResponse("hostname is: %s" % request.get_host())


def search_form(request):
    """
    搜索框
    """
    return render_to_response('search_form.html')

def search(request):
    """
    搜索框返回值
    """
    if  'q' in request.GET:
        message = 'you searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','noreply@example.com'),

            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contract_form.html',{
        'errors':errors,
    })

#def display_meta(request):
#    values = request.META.items()
#    values.sort()
#    html = []
#    for k,v in values:
#        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
#    return HttpResponse('<table>%s</table>' % '\n'.join(html))
#


#class Update_ServerList(View):
#    url = 'http://172.16.41.7:8000/mysite/api/saadmin/'
#
#    def get(self,request):
#        ServerList.objects.all().delete()
#        response = urllib2.urlopen(self.url)
#        for line in response:
#            SL = ServerList(kaifu_id=serverinfo[0],
#                       plat=serverinfo[1],
#                       server_id=serverinfo[2],
#                       server_name=serverinfo[3],
#                       open_time=serverinfo[4],
#                       domain=serverinfo[5],
#                       dx_ip=serverinfo[6],
#                       lt_ip=serverinfo[7],
#                       version=serverinfo[8],
#                       dfid=serverinfo[9],
#                       hefu_range=serverinfo[10])
#            SL.save()
#        return HttpResponse("OK")






