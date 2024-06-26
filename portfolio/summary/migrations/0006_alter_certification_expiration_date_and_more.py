# Generated by Django 5.0.2 on 2024-03-08 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='get_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_ext_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='period_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='period_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='period_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
