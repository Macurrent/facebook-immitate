
from django.contrib import admin
from django.urls import path
from . import views
from app1.views import SignUpView


urlpatterns = [
    path('', SignUpView.as_view(template_name='app1/index.html'), name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('post/', views.Post_new, name='post'),

]
