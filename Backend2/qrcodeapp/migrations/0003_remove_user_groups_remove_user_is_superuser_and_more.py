# Generated by Django 4.1.4 on 2022-12-13 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodeapp', '0002_user_delete_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]