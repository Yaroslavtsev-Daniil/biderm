# Generated by Django 4.1.6 on 2023-05-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/options/', verbose_name='картинка для слайдера'),
        ),
        migrations.AlterField(
            model_name='element',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/elements/', verbose_name='картинка для карточки элемента'),
        ),
        migrations.AlterField(
            model_name='option',
            name='category',
            field=models.ManyToManyField(to='calc.optionscategory', verbose_name='В категории'),
        ),
    ]
