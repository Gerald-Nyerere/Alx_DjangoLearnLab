from django.shortcuts import render
from rest_framework import generics, filters
from django_filters import rest_framework
from .models import Book
from rest_framework.exceptions import NotFound
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'author__name'] 

class CustomBookDetailView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    lookup_field = 'id' 
    
class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookUpdateView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id' 

class CustomBookDeleteView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id' 
    permission_classes = [IsAuthenticatedOrReadOnly]