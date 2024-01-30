# Generated by Django 5.0.1 on 2024-01-30 01:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_personaldetails_cv_alter_personaldetails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='heading',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='achievement',
            name='details',
            field=ckeditor.fields.RichTextField(),
        ),
    ]