# Generated by Django 3.2.4 on 2021-07-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0005_alter_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, upload_to='bb/%Y/%m/%d3794'),
        ),
    ]
