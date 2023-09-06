from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.Signup.as_view(), name="signup"),
]
