# Generated by Django 3.1.5 on 2021-01-11 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='users',
            name='date',
        ),
    ]
