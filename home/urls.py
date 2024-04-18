from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
     
]
