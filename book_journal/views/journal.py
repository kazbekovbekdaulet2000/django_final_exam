from rest_framework import generics
from book_journal.models.journal import Journal
from book_journal.permissions import AdminOrReadOnly
from book_journal.serializers.journal import JournalSerializer


class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (AdminOrReadOnly,)


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (AdminOrReadOnly,)
