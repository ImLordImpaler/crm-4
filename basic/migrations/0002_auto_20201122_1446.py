# Generated by Django 3.0.5 on 2020-11-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='responseType',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='response',
            field=models.CharField(choices=[('warm', 'warm'), ('normal', 'normal'), ('cold', 'cold')], default=None, max_length=10),
        ),
    ]
