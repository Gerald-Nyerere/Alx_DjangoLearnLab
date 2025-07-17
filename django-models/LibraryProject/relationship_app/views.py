from django.shortcuts import render
from django.views.generic import DetailView
from . models import Book, Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()  
    context = {'book_list': books}  
    return render(request, 'books/book_list.html', context)


class BookDetailView(DetailView):
    model = Library
    template_name = 'books/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['book'] = self.object.books.all() 
        return context