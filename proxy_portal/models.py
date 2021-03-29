from django.db import models

# Create your models here.
from django.urls import reverse


class ProjectList(models.Model):
    project_name = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name[:50]


class ProxyList(models.Model):
    id = models.AutoField(primary_key=True)
    proxy_id = models.IntegerField(default=1)
    project = models.ForeignKey(ProjectList, on_delete=models.CASCADE)
    proxy_port_in = models.IntegerField(default=32000)
    proxy_port_out = models.IntegerField(default=32000)
    proxy_name = models.CharField(max_length=255)
    fp_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    stop_date = models.DateTimeField(default='28.03.2021 21:35:38')
    start_date = models.DateTimeField(default='06.06.2021 05:05:25')
    proxy_pid = models.IntegerField(default=1)
    status = models.BooleanField

    def __str__(self):
        return self.proxy_name[:50]

    def get_absolute_url(self):
        return reverse('proxy_detail', args=[str(self.id)])
