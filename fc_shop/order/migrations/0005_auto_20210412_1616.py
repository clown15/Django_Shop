# Generated by Django 3.1.5 on 2021-04-12 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20210216_2240'),
        ('order', '0004_auto_20210406_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fcuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='고객'),
        ),
    ]