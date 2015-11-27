from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class BookSerializer(serializers.ModelSerializer):
    search_url = serializers.SerializerMethodField('get_search_url')
    title = serializers.Field(source='title')
    class Meta:
        model = Book
        fields = ('id','title','isbn','search_url')

    def get_search_url(self,obj):
        return 'Url {0}'.format(obj.isbn)


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True,required=False)
    class Meta:
        model = Author
        fields = ('id','first_name','last_name','books')
