# Generated by Django 5.0.3 on 2024-04-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('committee', models.CharField(max_length=100)),
                ('reason', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
