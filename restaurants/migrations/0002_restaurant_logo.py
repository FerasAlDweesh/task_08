# Generated by Django 2.1.5 on 2019-10-07 16:32

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
