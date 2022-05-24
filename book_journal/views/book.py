from rest_framework import generics
from book_journal.models.book import Book
from book_journal.permissions import AdminOrReadOnly
from book_journal.serializers.book import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AdminOrReadOnly,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AdminOrReadOnly,)
