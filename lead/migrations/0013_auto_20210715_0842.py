# Generated by Django 3.2.5 on 2021-07-15 03:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0012_auto_20210714_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='dete_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
