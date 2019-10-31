from django.contrib import admin
from .models import AuthorEditorTranslator, Book

@admin.register(AuthorEditorTranslator)
class AuthorEditorTranslatorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
