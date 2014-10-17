from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import View
from models import *
import urllib2

# Create your views here.
class Update_ServerList(View):
    url = 'http://172.16.41.7/mysite/api/saadmin/'

    def get(self,request):
        ServerList.objects.all().delete()
        response = urllib2.urlopen(self.url)
        for line in response:
            SL = ServerList(kaifu_id=serverinfo[0],
                       plat=serverinfo[1],
                       server_id=serverinfo[2],
                       server_name=serverinfo[3],
                       open_time=serverinfo[4],
                       domain=serverinfo[5],
                       dx_ip=serverinfo[6],
                       lt_ip=serverinfo[7],
                       version=serverinfo[8],
                       dfid=serverinfo[9],
                       hefu_range=serverinfo[10])
            SL.save()
        return HttpResponse("OK")




