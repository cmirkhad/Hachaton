from django.contrib import admin

# Register your models here.
from Hachaton.bookadmin.models import Books, Author

admin.site.register(Books)
admin.site.register(Author)