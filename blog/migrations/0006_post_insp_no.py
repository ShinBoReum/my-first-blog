# Generated by Django 2.0.13 on 2023-10-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231018_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='INSP_NO',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
