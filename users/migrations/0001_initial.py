# Generated by Django 4.2.1 on 2023-05-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]
