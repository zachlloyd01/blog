# Generated by Django 2.1.3 on 2018-12-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default='Preview here!', max_length=300),
        ),
    ]
