# Generated by Django 3.1.6 on 2021-02-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='question_image',
            field=models.ImageField(blank=True, upload_to='question'),
        ),
    ]
