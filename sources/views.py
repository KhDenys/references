from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .models import AuthorEditorTranslator, Book
from .serializers import BookSerializer


def index(request):
    return render(request, 'index.html')


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
