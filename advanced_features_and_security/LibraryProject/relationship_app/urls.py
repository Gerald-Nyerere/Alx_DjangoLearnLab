from django.urls import path
from .views import list_all_books, LibraryDetailView
from .views import list_books
from django.contrib.auth import views as auth_views
from . import views
from relationship_app.views.admin_view import admin_dashboard
from relationship_app.views.librarian_view import librarian_dashboard
from relationship_app.views.member_view import member_dashboard


urlpatterns = [
    path('books/', list_all_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/', admin_dashboard, name='admin_view'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_view'),
    path('member-dashboard/', member_dashboard, name='member_view'),

    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),
]
