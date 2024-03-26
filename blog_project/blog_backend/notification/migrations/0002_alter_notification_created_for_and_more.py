# Generated by Django 4.2.11 on 2024-03-26 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type_of_notification',
            field=models.CharField(choices=[('new_friendrequest', 'New friend request'), ('accepted_friendrequest', 'Accepted friend request'), ('rejected_friendrequest', 'Rejected friend request'), ('post_comment', 'Post comment'), ('post_like', 'Post like')], max_length=50),
        ),
    ]
