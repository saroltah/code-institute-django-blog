# Generated by Django 4.2.10 on 2024-03-11 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_post_updated_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
