# Generated by Django 4.2.5 on 2023-12-12 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=765)),
                ('skills', models.CharField(max_length=255)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_1', models.URLField(blank=True)),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_2', models.URLField(blank=True)),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_3', models.URLField(blank=True)),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_4', models.URLField(blank=True)),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_5', models.URLField(blank=True)),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_6', models.URLField(blank=True)),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_7', models.URLField(blank=True)),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='portfolio/%Y/%m/%d/')),
                ('link_8', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
                'ordering': ['-creation_date', 'user'],
            },
        ),
    ]
