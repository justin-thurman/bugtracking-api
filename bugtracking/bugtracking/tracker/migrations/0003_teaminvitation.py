# Generated by Django 3.0.11 on 2020-11-30 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_project_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamInvitation',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Declined')], default=1)),
                ('invitee_email', models.EmailField(max_length=254)),
                ('message_text', models.TextField()),
                ('invitee', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_team_invites', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_team_invites', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Team')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]