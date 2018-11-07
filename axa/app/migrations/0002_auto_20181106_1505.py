# Generated by Django 2.0 on 2018-11-06 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fai', models.CharField(max_length=25)),
                ('tempsdown', models.CharField(max_length=40)),
                ('compensation', models.CharField(max_length=40)),
                ('cause', models.CharField(max_length=400)),
                ('entreprise', models.CharField(default='{{ user.username }}', max_length=40)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'litige',
                'ordering': ['creation_date'],
            },
        ),
        migrations.DeleteModel(
            name='Litige',
        ),
    ]
