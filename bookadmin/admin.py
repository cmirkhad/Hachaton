from django.contrib import admin

from .models import Books, Author, Publisher, Category

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Books)
admin.site.register(Category)




