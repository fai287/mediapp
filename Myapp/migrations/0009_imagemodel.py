# Generated by Django 5.1.3 on 2024-11-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]