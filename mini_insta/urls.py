from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile'),
    path('create/', views.ProfileCreateView.as_view(), name='create_profile'),
    path('log_in/', views.login, name='login'),
]
