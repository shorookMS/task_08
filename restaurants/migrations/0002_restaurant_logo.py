# Generated by Django 2.0.4 on 2018-10-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
