# Generated by Django 3.0.7 on 2021-04-19 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relationship',
            name='friends',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='recipient'),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='chatgroupmessage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_group_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatgroupmessage',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.ChatGroup'),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='member',
            field=models.ManyToManyField(related_name='chat_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
