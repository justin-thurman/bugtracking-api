# Generated by Django 3.0.11 on 2020-12-01 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_teaminvitation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teaminvitation',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='teaminvitation',
            unique_together={('invitee_email', 'team')},
        ),
    ]
