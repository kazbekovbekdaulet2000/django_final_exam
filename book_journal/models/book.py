from django.db import models
from common.abstact import BookJournalBase
from django.contrib.postgres.fields import ArrayField


class Book(BookJournalBase):
  num_pages = models.PositiveIntegerField()
  genre = ArrayField(models.CharField(max_length=255))

  class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
