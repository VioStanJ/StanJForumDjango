# Generated by Django 2.1.5 on 2019-01-22 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['date']},
        ),
    ]
