from django.db import models

from .book import Book


class AuthorEditorTranslator(models.Model):
    AUTHOR = 'au'
    EDITOR = 'ed'
    TRANSLATOR = 'tr'

    AUTHOR_EDITOR_TRANSLATOR_CHOICES = [
        (AUTHOR, 'author'),
        (EDITOR, 'editor'),
        (TRANSLATOR, 'translator')
    ]

    book = models.ForeignKey(Book, related_name='authors', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Ім’я', max_length=50)
    last_name = models.CharField(verbose_name='Прізвище', max_length=50)
    patronymic = models.CharField(verbose_name='По батькові', max_length=50)
    _type = models.CharField(max_length=2, choices=AUTHOR_EDITOR_TRANSLATOR_CHOICES, default=AUTHOR)
    lang = models.CharField(max_length=20, blank=True, null=True)
