# Generated by Django 2.0.7 on 2018-08-13 21:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('neekap', '0002_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(default='none')),
            ],
        ),
    ]
