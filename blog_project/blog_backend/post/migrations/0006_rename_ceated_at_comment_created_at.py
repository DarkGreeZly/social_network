# Generated by Django 4.2.11 on 2024-03-15 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='ceated_at',
            new_name='created_at',
        ),
    ]
