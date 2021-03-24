# Generated by Django 3.1.7 on 2021-03-24 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ogrn', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_brand', models.CharField(max_length=300)),
                ('model_name', models.CharField(max_length=300)),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('top_speed', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('horsepower', models.IntegerField()),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autotrade.dealer')),
            ],
        ),
    ]
