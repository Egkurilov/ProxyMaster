# Generated by Django 3.1.7 on 2021-03-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_portal', '0003_auto_20210328_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
            ],
        ),
    ]
