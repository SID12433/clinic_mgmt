# Generated by Django 4.2.5 on 2024-03-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_appointment_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
