# Generated by Django 5.0.1 on 2024-02-04 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=255)),
                ('user_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdetails')),
            ],
        ),
    ]
