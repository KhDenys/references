from rest_framework import serializers

from .models import AuthorEditorTranslator, Book


class AETSerializer(serializers.ModelSerializer):
    '''Serializer for AuthorEditorTranslator model'''
    class Meta:
        model = AuthorEditorTranslator
        exclude = ('book',)


class BookSerializer(serializers.ModelSerializer):
    a_e_t = serializers.SerializerMethodField(read_only=True)
    authors = AETSerializer(many=True, write_only=True, allow_null=True)
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        print('create was called')
        a_e_t = validated_data.pop('authors', None)
        print(validated_data)
        book = Book.objects.create(**validated_data)
        if a_e_t is not None:
            book_dict = {'book_id': book.id}
            for item in a_e_t:
                item.update(book_dict)
            AuthorEditorTranslator.objects.bulk_create(
                [AuthorEditorTranslator(**item) for item in a_e_t]
            )

        return book

    def get_a_e_t(self, book):
        '''Get serialized data of AuthorEditorTranslator'''
        authors = book.authors.all()
        return AETSerializer(authors, many=True).data
