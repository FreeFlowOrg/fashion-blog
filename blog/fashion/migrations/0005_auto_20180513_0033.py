# Generated by Django 2.0.5 on 2018-05-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0004_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Beauty', 'Beauty'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Fitness', 'Fitness')], default='Fashion', max_length=10),
        ),
    ]
