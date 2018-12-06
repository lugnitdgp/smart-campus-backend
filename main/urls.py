from django.urls import include, path
from main import views

urlpatterns = [
    path('users/all/', views.get_all_users, name='get_all_users'),
    path('users/<slug:username>/', views.get_user, name='get_user')
]

