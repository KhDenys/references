from django.urls import path

from .views import download_docx


urlpatterns = [
    path('', download_docx)
]