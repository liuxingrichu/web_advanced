from django.db import models


# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=32)
    name_en = models.CharField(max_length=64, default='RDD')


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4', db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to='Business', to_field='id')


class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")

# class HostToApp(models.Model):
#     hobj = models.ForeignKey(to="Host", to_field="nid")
#     aobj = models.ForeignKey(to="Application", to_field="id")
