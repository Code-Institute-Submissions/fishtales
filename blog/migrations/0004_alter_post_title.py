# Generated by Django 3.2.14 on 2022-07-29 11:39

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220726_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=blog.models.default_title, max_length=200, unique=True),
        ),
    ]
