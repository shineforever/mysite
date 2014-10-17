from django.db import models

# Create your models here.


class ServerList(models.Model):
    kaifu_id = models.IntegerField()
    plat = models.CharField(max_length=30)
    server_id = models.IntegerField()
    server_name = models.CharField(max_length=30)
    open_time = models.DateField()
    domain = models.CharField(max_length=50)
    dx_ip = models.IPAddressField()
    lt_ip = models.IPAddressField()
    version = models.CharField(max_length=10)
    dfid = models.IntegerField()
    hefu_range = models.TextField()


