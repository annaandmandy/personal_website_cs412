from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile')
]
