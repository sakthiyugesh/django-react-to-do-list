# Generated by Django 5.0.1 on 2024-01-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lists',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
