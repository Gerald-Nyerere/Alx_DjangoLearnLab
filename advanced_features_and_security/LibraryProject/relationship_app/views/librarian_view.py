from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.utils import is_librarian

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_view.html')
