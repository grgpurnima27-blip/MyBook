

from django.urls import path 
from .views import home, detail, add, edit, delete

urlpatterns = [
    path('', home, name='book_list'),                   # List all books
    path('detail/<int:id>/', detail, name='detail'),    # Book detail
    path('create/', add, name='create'),               # Add new book
    path('edit/<int:id>/', edit, name='edit'),         # Edit book
    path('delete/<int:id>/', delete, name='delete'),   # Delete book
]