# Generated by Django 3.2.2 on 2021-05-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0009_auto_20210513_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxylist',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='proxylist',
            name='stop_date',
            field=models.DateTimeField(),
        ),
    ]