from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class BookSerializer(serializers.ModelSerializer):
    title = serializers.Field(source='title')
    class Meta:
        model = Book
        fields = ('id','title','isbn')


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ('id','first_name','last_name','books')
