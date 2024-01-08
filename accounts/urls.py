from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("profile_change/<int:pk>", views.UserChangeView.as_view(), name="profile_change"),
]