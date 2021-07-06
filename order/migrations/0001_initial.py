# Generated by Django 3.1.5 on 2021-07-02 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('total_price', models.IntegerField(verbose_name='가격')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='주문자')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'order',
            },
        ),
    ]