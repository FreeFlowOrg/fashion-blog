# Generated by Django 2.0.5 on 2018-05-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0008_comment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
