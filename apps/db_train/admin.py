from django.contrib import admin
from .models import Author, Tag, Entry, AuthorProfile

admin.site.register(Author)

admin.site.register(Tag)

admin.site.register(Entry)
