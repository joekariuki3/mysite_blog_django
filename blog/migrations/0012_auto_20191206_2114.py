# Generated by Django 2.2.7 on 2019-12-06 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191206_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approve_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
