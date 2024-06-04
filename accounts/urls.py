from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path(
        "profile_change/<int:pk>/",
        views.UserChangeView.as_view(),
        name="profile_change",
    ),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("contact/result/", views.ContactResultView.as_view(), name="contact_result"),
]
