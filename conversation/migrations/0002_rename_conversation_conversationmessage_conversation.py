# Generated by Django 4.2.16 on 2024-09-19 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='Conversation',
            new_name='conversation',
        ),
    ]
