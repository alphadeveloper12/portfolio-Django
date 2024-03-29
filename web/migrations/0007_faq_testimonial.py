# Generated by Django 5.0.1 on 2024-01-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_story_delivered_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='testimonial_images/')),
                ('designation', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
    ]
