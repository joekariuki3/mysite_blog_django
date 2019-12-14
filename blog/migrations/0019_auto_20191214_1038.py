# Generated by Django 3.0 on 2019-12-14 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191214_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='<django.db.models.fields.CharField>8fe34596204c1b64cc299b6fc841c2', unique=True),
        ),
    ]
