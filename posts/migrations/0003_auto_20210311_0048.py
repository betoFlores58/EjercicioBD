# Generated by Django 3.1.7 on 2021-03-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
