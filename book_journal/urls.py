from django.urls import path
from book_journal.views.book import BookDetail, BookList
from book_journal.views.journal import JournalDetail, JournalList


urlpatterns = [
  path('books/', BookList.as_view()),
  path('books/<int:id>/', BookDetail.as_view()),
  path('journals/', JournalList.as_view()),
  path('journals/<int:id>/', JournalDetail.as_view()),
]
