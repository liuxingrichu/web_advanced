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
