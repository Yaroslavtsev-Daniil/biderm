# Generated by Django 4.1.6 on 2023-05-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_option_image_alter_element_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='option',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='optionscategory',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок'),
        ),
    ]
