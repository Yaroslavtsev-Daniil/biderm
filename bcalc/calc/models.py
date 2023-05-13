from django.db import models

from tinymce.models import HTMLField


# def get_self_id(OptionsCategory):
#     return OptionsCategory.id
# Попытка выводить для выбора значения по умолчанию только тех опций, что привязаны к категории.


class OptionsCategory(models.Model):
    title = models.CharField('Название', max_length=80, null=False, blank=False)
    sort = models.IntegerField('Позиция в списке', null=True, blank=True)
    subtitle = models.TextField('Подзаголовок', null=True, blank=True)

    default_value = models.ForeignKey(
        'Option',
        on_delete=models.SET_NULL,
        # limit_choices_to={'category': OptionsCategory.pk},
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    def get_options_list(self):
        options_list = Option.objects.filter(category=self)
        return options_list
    #
    # def get_self_id(self):
    #     return self.pk


class Option(models.Model):
    title = models.CharField('Название', max_length=80, null=False, blank=False)
    sort = models.IntegerField('Позиция в списке', null=True, blank=True)
    subtitle = models.TextField('Подзаголовок', null=True, blank=True)
    cost = models.IntegerField('Цена ', null=True, blank=True)
    image = models.ImageField(
        verbose_name='картинка для слайдера',
        upload_to='images/options/',
        null=True, blank=True,
    )
    category = models.ManyToManyField(
        OptionsCategory,
        verbose_name=u'В категории')

    def __str__(self):
        return self.title


class Element(models.Model):
    title = models.CharField('Название', max_length=80, null=False, blank=False)
    sort = models.IntegerField('Позиция в списке', null=True, blank=True)
    subtitle = models.TextField('Подзаголовок', null=True, blank=True)
    image = models.ImageField(
        verbose_name='картинка для карточки элемента',
        upload_to='images/elements/',
        null=True, blank=True,
    )

    coefficient = models.DecimalField(
        'Коэфф для расчета ',
        default=1.00, decimal_places=2, max_digits=3,
        null=False, blank=False
    )

    def __str__(self):
        return self.title


# class Parameter(models.Model):
#     title = models.CharField('Название', max_length=80, null=False, blank=False)
#
#     value = models.DecimalField('Значение, мм', decimal_places=0, max_digits=4, null=True, blank=True)
#     default_value = models.DecimalField('Значение по умолчанию, мм', decimal_places=0, max_digits=4, null=True, blank=True)
#     # Relations
#     Parameter = models.ForeignKey('Parameter', on_delete=models.SET_NULL, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

