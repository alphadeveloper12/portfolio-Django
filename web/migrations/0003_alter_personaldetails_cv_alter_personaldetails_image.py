# Generated by Django 5.0.1 on 2024-01-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_personaldetails_cv_alter_personaldetails_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='cv',
            field=models.FileField(upload_to='cv_pdfs/'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]