# Generated by Django 3.2.3 on 2021-06-22 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_changeurl_fullurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changeurl',
            old_name='shorturl',
            new_name='slug',
        ),
    ]
