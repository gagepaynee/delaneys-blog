# Generated by Django 2.1.2 on 2018-10-07 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181007_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bg_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]