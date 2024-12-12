# Generated by Django 5.1.3 on 2024-11-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0006_rename_phone_contact_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(blank=True, default='General', max_length=255, null=True),
        ),
    ]