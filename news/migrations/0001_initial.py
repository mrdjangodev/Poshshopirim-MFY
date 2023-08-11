# Generated by Django 4.2.4 on 2023-08-10 14:36

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_alter_worker_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Yangilik Turi',
                'verbose_name_plural': 'Yangilik Turlari',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Sarlavha')),
                ('image', models.ImageField(upload_to='news/', verbose_name='rasm')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='Yangilikning kontentini shu yerga yozasiz')),
                ('views', models.PositiveBigIntegerField(default=0, verbose_name="Ko'rishlar soni")),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Yuklangan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worker', verbose_name='Muallif')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newscategory', verbose_name='Yangilik Turi')),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
                'ordering': ['-published_at'],
            },
        ),
    ]