# Generated by Django 5.0.1 on 2024-01-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_achievement_heading_alter_achievement_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='detail_image',
            field=models.ImageField(default=1, upload_to='achievement_detail/'),
            preserve_default=False,
        ),
    ]
