# Generated by Django 2.0.13 on 2023-10-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_max_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='MORT_WRTH',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='MORT_LOCPL',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
