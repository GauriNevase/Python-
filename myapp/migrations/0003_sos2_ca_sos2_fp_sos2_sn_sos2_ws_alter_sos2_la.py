# Generated by Django 4.1.7 on 2023-04-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_sos_sos2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sos2',
            name='Ca',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sos2',
            name='Fp',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sos2',
            name='Sn',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sos2',
            name='Ws',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sos2',
            name='La',
            field=models.CharField(max_length=100),
        ),
    ]