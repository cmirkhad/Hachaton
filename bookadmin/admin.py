from django.contrib import admin

from .models import Books, Author, Publisher, Category,ReservedBookItem

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(ReservedBookItem)




