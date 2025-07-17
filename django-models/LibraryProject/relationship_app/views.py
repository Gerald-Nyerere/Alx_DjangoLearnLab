from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()  
    context = {'book_list': books}  
    return render(request, 'relationship_app/list_books.html', context)


class BookDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['book'] = self.object.books.all() 
        return context
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: log in after registration
            return redirect('list_all_books')  # Redirect to any view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
