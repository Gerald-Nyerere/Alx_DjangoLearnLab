from django.urls import path
from . import views 

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-registration"),
    path("login/", views.LoginView.as_view(), name="user-login"),
    path("profile/", views.ProfileView.as_view(), name="user-profile")
]
