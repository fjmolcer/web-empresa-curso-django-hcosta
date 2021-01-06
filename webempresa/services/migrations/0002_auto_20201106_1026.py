# Generated by Django 3.1.3 on 2020-11-06 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='service',
            name='content',
            field=models.TextField(default='', verbose_name='Contenido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtítulo'),
        ),
    ]