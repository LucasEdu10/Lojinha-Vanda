# Generated by Django 2.0 on 2021-04-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_fabric'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='picture_fabric',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]