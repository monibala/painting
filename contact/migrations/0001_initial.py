# Generated by Django 4.0.5 on 2022-11-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(max_length=500, null=True)),
                ('msg', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
