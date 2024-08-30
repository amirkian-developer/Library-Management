from django.urls import path,include
from . import views

app_name='library'

urlpatterns = [
    path('',views.start,name='start'),
    path('books/',views.home,name='home'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('edit/<int:id>/'  , views.edit_book,   name='edit_book'),
    path('add/', views.add_book,name='add_book'),
    # path('search/', views.search_books, name='search_books'),
]



