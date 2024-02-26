from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


urlpatterns = [
    path('register/', views.register),
    path('login/', views.loginView.as_view()),
    path('refresh/', TokenObtainPairView.as_view()),
]

