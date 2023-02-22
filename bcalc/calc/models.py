from django.db import models

from tinymce.models import HTMLField


class Parameter(models.Model):
    name = models.CharField('Название', max_length=80, null=False, blank=False)
    slug = models.SlugField('Ссылка', max_length=255, unique=True, db_index=True)
    round_image = models.ImageField(
        verbose_name='Круглая картинка для навигации',
        upload_to='images/',
        null=True, blank=True,
    )
    #default_option =

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField('Название', max_length=80, null=False, blank=False)
    image = models.ImageField(
        verbose_name='картинка для слайдера',
        upload_to='images/options/',
        null=True, blank=True,
    )
    title = models.CharField('Мета title', max_length=150, null=True, blank=False)
    description = HTMLField('Описание', null=True, blank=True)
    coefficient = models.DecimalField('Коэфф для расчета ', decimal_places=2, max_digits=3, null=True, blank=True)

    # Relations
    Parameter = models.ForeignKey('Parameter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField('Название', max_length=80, null=False, blank=False)
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='images/elements/',
        null=True, blank=True,
    )
    title = models.CharField('Мета title', max_length=150, null=True, blank=False)
    description = HTMLField('Описание', null=True, blank=True)
    coefficient = models.DecimalField('Коэфф для расчета ', decimal_places=2, max_digits=3, null=True, blank=True)

    def __str__(self):
        return self.name
