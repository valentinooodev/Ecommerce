# Generated by Django 3.2.5 on 2021-07-27 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]