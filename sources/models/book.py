from django.db import models 


class Book(models.Model):
    name = models.CharField(verbose_name='Назва книги', max_length=255, db_index=True)
    book_type = models.CharField(verbose_name='Тип книги', max_length=50, blank=True, null=True)
    number = models.SmallIntegerField(verbose_name='Номер видання', blank=True, null=True)
    publisher = models.CharField(verbose_name='Видавництво', max_length=255, blank=True, null=True)
    city_of_publication = models.CharField(verbose_name='Місто видання', max_length=255, blank=True, null=True)
    year = models.SmallIntegerField(verbose_name='Рік видання', blank=True, null=True)
    number_of_pages = models.PositiveSmallIntegerField(verbose_name='Кількість сторінок', blank=True, null=True)
    extra_info = models.CharField(verbose_name='Додаткова інформація', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        number = f' № {self.number}' if self.number else ''
        year = f' {self.year}p.' if self.year else ''
        return f'{self.name}{number}{year}'
