from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLoginView
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
    path('products/', views.product_list, name='product_list'),
    
]
