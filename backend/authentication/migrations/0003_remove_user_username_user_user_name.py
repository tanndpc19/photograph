# Generated by Django 5.0.3 on 2024-03-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userName',
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
