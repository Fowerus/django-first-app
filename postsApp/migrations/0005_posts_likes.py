# Generated by Django 3.1.5 on 2021-01-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0004_auto_20210107_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.BinaryField(blank=True),
        ),
    ]