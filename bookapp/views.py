from bookapp.models import Book
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm, UpdateBookForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):   # Let's use class-based views instead
    model = Book
    template_name = 'home.html'
    ordering = ['-id']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    # Now that we have added this info to forms.py and imported out form_class here, we no longer need the fields specified here
    #fields = '__all__'
    #fields = ('title', 'author', 'discussion_date', 'category', 'summary', 'is_current', 'purchase_link')

class UpdateBookView(UpdateView):
    model = Book
    form_class = UpdateBookForm
    template_name = 'update_book.html'
    #fields = ('title', 'author', 'discussion_date', 'category', 'summary', 'is_current', 'purchase_link')

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('home')