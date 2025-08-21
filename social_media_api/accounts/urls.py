from django.urls import path
from . import views 
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-registration"),
    path("login/", views.LoginView.as_view(), name="user-login"),
    path("profile/", views.ProfileView.as_view(), name="user-profile"),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
