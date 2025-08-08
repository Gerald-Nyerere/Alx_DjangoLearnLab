from django.shortcuts import render
from rest_framework import generics
from .models import Book
from rest_framework.exceptions import NotFound
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# Create your views here.
class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] 

class CustomBookDetailView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] 
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