# Generated by Django 2.1.5 on 2019-01-22 01:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('fonction', models.CharField(max_length=60)),
                ('pass1', models.CharField(max_length=100)),
                ('pass2', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
            ],
        ),
    ]
