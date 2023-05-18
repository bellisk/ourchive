# Generated by Django 4.1 on 2022-08-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20200904_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fingerguns',
            old_name='user',
            new_name='work',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='audio_length',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='replies',
            field=models.ManyToManyField(to='api.message'),
        ),
    ]
