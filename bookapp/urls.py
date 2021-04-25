from django.urls import path
# from . import views
from .views import HomeView, BookDetailView, AddBookView, UpdateBookView, DeleteBookView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),   #because we are using class-based views
    path('book/<int:pk>', BookDetailView.as_view(), name="book_details"),
    path('add_book/', AddBookView.as_view(), name="add_book"),
    path('book/<int:pk>/edit', UpdateBookView.as_view(), name="update_book"),
    path('book/<int:pk>/delete', DeleteBookView.as_view(), name="delete_book"),
]
