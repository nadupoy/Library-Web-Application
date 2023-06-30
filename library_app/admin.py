from django.contrib import admin

# Register your models here.
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "genre"]

admin.site.register(Book, BookAdmin)
admin.site.register(Author)