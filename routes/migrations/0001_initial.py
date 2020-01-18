# Generated by Django 3.0.2 on 2020-01-18 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ('route_number',),
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=200)),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.Route')),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_name', models.CharField(max_length=200)),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.Route')),
            ],
        ),
    ]