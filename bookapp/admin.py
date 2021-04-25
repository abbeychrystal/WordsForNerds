from django.contrib import admin
from .models import Book

# Register your models here. Allows our book's entries to be accessible from the admin area
admin.site.register(Book)