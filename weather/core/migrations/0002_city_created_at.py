# Generated by Django 4.1.6 on 2023-04-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]