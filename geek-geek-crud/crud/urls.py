from django.urls import path
from .views import home_view, delete_book_view, update_book_view

app_name = 'books'

urlpatterns = [
    path('', home_view, name='home'),
    path('delete/<id>', delete_book_view, name='delete_book_view'),
    path('update/<id>', update_book_view, name='update_book_view')
]
