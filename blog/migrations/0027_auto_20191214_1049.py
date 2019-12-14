# Generated by Django 3.0 on 2019-12-14 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20191214_1047'),
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
            field=models.SlugField(default='6438e7e74dfc4b8e68a361bee1dcf6'),
        ),
    ]
