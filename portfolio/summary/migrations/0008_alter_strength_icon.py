# Generated by Django 5.0.2 on 2024-03-09 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0007_alter_strength_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strength',
            name='icon',
            field=models.FileField(upload_to='strengths_logo/', validators=[django.core.validators.FileExtensionValidator(['png', 'svg'])]),
        ),
    ]