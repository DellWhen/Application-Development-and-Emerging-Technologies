# Generated by Django 5.1.1 on 2024-09-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=10)),
                ('coordinates', models.CharField(max_length=50)),
                ('temperature', models.FloatField()),
                ('pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('weather_main', models.CharField(max_length=50)),
                ('weather_description', models.CharField(max_length=150)),
                ('weather_icon', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]