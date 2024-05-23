from django.urls import path
from . import views
from .api_views import CustomUserCreate, CustomUserRetrieve

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('register/', views.register, name='register'),
    path('api/users/', CustomUserCreate.as_view(), name='user-create'),
    path('api/users/<int:pk>/', CustomUserRetrieve.as_view(), name='user-retrieve'),
]