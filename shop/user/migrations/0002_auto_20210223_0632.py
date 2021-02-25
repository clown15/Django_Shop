# Generated by Django 3.1.5 on 2021-02-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('admin', '관리자'), ('user', '고객')], default='user', max_length=16, verbose_name='등급'),
        ),
    ]
