from django.contrib import admin
from .models import Book

@admin.register(Book)
class booksadmin(admin.Modeladmin):
list_display =('id','title','author','rating')
search_fields = ('title','author')
list_filter = ('rating',)