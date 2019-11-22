from rest_framework import serializers
from bitblack.website.book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description"]
        