# Generated by Django 2.0.13 on 2023-10-18 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231016_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumb_nail_des',
            new_name='suss_rate',
        ),
    ]