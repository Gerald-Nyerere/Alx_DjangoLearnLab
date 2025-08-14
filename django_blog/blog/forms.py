from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # author will be set automatically
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.author = user  # automatically set author
        if commit:
            instance.save()
        return instance
    

    #comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post',  'author', 'content', 'created_at', 'updated_at']