# Generated by Django 3.1.7 on 2021-03-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0007_auto_20210328_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxylist',
            name='proxy_pid',
            field=models.IntegerField(default=1),
        ),
    ]
