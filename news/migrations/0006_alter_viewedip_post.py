# Generated by Django 4.2.4 on 2023-08-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewedip',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='viewed_ips', to='news.post'),
        ),
    ]
