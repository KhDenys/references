from django.http import FileResponse

from sources.models import Book
from .producer_docx import generate_docx


def download_docx(request):
    books = Book.objects.prefetch_related('authors')
    docx_file = generate_docx(books)
    response = FileResponse(open(docx_file, 'rb'))

    return response
