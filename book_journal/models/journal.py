from django.db import models
from common.abstact import BookJournalBase
from common.constants import JOURNAL_TYPE


class Journal(BookJournalBase):
  publisher = models.CharField(max_length=255)
  type = models.PositiveIntegerField(choices=JOURNAL_TYPE)

  class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
