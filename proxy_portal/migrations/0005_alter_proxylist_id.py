# Generated by Django 3.2 on 2021-04-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0004_auto_20210404_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxylist',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
