# Generated by Django 4.1.2 on 2022-11-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='blog_pictures'),
        ),
    ]
