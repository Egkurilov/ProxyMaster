from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class ProjectList(models.Model):
    project_name = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name[:50]


class ProxyList(models.Model):
    def __init__(self):
        proxy_id = 1
        project_id = 1
        proxy_port_in = 1
        proxy_port_out = 1
        proxy_name = 5
        fp_name = 4
        author = 3
        stop_date = 1
        start_date = 1
        status = 1

    id = models.AutoField(primary_key=True)
    proxy_id = models.IntegerField(default=1)
    project = models.ForeignKey(ProjectList, on_delete=models.CASCADE)
    proxy_port_in = models.IntegerField(validators=[MinValueValidator(32000), MaxValueValidator(34000)])
    proxy_port_out = models.IntegerField(default=32000)
    proxy_name = models.CharField(max_length=255)
    fp_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    stop_date = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    proxy_pid = models.IntegerField(default=1)
    status = models.BooleanField

    def __str__(self):
        return self.proxy_name[:50]

    def get_absolute_url(self):
        return reverse('proxy_detail', args=[str(self.id)])
