# Generated by Django 2.2.4 on 2019-08-11 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0002_suser_level'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
    ]
