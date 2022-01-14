# Generated by Django 3.2.11 on 2022-01-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('customerName', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('province', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
            ],
        ),
    ]