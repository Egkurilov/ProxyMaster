# Generated by Django 3.1.7 on 2021-04-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0005_auto_20210411_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxylist',
            name='start_date',
            field=models.DateTimeField(default='11/04/2021 23:57'),
        ),
        migrations.AlterField(
            model_name='proxylist',
            name='stop_date',
            field=models.DateTimeField(default='11/04/2021 23:57'),
        ),
    ]
