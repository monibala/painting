# Generated by Django 4.0.5 on 2022-10-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_types',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
