# Generated by Django 5.0.4 on 2025-03-23 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_alter_character_house_alter_character_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.house'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='character',
            name='patronus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='wand',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
