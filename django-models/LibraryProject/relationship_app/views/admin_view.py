from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.utils import is_admin

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_view.html')