# Generated by Django 3.2 on 2021-04-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0007_merge_0005_alter_proxylist_id_0006_auto_20210411_2357'),
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
