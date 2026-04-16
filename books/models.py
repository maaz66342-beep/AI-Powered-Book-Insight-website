from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)
    description = models.TextField(black=True)
    book_url = models.TextField(blank=True)

    def __str__(self):
        return self.titles