# Generated by Django 4.0 on 2021-12-15 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='cover',
            field=models.ImageField(blank=True, upload_to='resources/cover'),
        ),
    ]
