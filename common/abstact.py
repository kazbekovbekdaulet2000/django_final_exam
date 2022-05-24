from django.db import models

class AbstractCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class AbstractUpdatedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BookJournalBase(AbstractCreatedModel):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(null=False)
    description = models.TextField(max_length=4096) 

    class Meta:
        abstract = True
