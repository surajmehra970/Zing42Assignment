# Generated by Django 4.0.1 on 2022-03-31 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateBhav',
            fields=[
                ('Date', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Securities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SYMBOL', models.CharField(max_length=15)),
                ('NAME_OF_COMPANY', models.CharField(max_length=100)),
                ('SERIES', models.CharField(max_length=2)),
                ('DATE_OF_LISTING', models.TextField(max_length=20)),
                ('PAID_UP_VALUE', models.IntegerField()),
                ('MARKET_LOT', models.IntegerField()),
                ('ISIN_NUMBER', models.CharField(max_length=15)),
                ('FACE_VALUE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bhav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SYMBOL', models.CharField(max_length=15)),
                ('SERIES', models.CharField(max_length=2)),
                ('OPEN', models.FloatField()),
                ('HIGH', models.FloatField()),
                ('LOW', models.FloatField()),
                ('CLOSE', models.FloatField()),
                ('LAST', models.FloatField()),
                ('PREVCLOSE', models.FloatField()),
                ('TOTTRDQTY', models.IntegerField()),
                ('TOTTRDVAL', models.FloatField()),
                ('TOTALTRADES', models.IntegerField()),
                ('ISIN', models.CharField(max_length=25)),
                ('TIMESTAMP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataapi.datebhav')),
            ],
        ),
    ]
