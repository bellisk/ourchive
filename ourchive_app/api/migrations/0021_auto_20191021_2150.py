# Generated by Django 2.2.6 on 2019-10-21 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20191020_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['number']},
        ),
    ]
