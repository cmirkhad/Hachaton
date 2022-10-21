from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BooksViewSet, AuthorViewSet, PublisherViewSet, CatygoryViewSet

bookadmin_router = DefaultRouter()

bookadmin_router.register(r'books', BooksViewSet)
bookadmin_router.register(r'category', CatygoryViewSet)
bookadmin_router.register(r'publisher', PublisherViewSet)
bookadmin_router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(bookadmin_router.urls))
]
