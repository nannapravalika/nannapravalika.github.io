# Generated by Django 4.0.4 on 2022-05-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_userbookticketmodel_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomplaintmodel',
            name='user',
        ),
        migrations.AlterField(
            model_name='userbookticketmodel',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userbookticketmodel',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]