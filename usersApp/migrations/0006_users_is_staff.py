# Generated by Django 3.1.5 on 2021-01-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0005_auto_20210111_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
