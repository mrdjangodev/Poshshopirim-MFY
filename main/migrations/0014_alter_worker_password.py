# Generated by Django 4.2.4 on 2023-08-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_worker_options_alter_worker_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='password',
            field=models.CharField(default='I3rz3Eq0', help_text='Ushbu parol         Xodimning tizimga kirishida ishlatiladi', max_length=10, verbose_name='Parol'),
        ),
    ]
