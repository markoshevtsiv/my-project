from django.contrib import admin

# Register your models here.
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'pages', 'available', 'user')
    list_filter = ('publication_date', 'available')
    search_fields = ('title')


admin.site.register(Book, BookAdmin)