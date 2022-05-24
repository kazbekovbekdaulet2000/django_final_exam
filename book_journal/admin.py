from django.contrib import admin
from book_journal.models.book import Book

from book_journal.models.journal import Journal

# Register your models here.
admin.site.register([Book, Journal])