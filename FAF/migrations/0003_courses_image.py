# Generated by Django 4.2.7 on 2024-02-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAF', '0002_remove_courses_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, default='book.jpg', upload_to='media'),
        ),
    ]
