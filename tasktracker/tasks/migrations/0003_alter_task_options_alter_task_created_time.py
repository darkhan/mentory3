# Generated by Django 5.0.1 on 2024-01-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='task',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
