from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_user_account', views.create_user_account, name='create_user_account'),
    path('update_user_account/<int:pk>/', views.update_user_account, name='update_user_account'),
    path('delete_user_account/<int:pk>/', views.delete_user_account, name='delete_user_account'),
    path('list_user_account/<int:pk>/', views.list_user_account, name='list_user_account'),
    path('create_user_data/<int:pk>/', views.create_user_data, name='create_user_data'),
    path('create_entry/<int:pk>/', views.create_entry, name='create_entry'),
    path('list_user_data/<int:pk>/', views.list_user_data, name='list_user_data'),
    path('update_user_data/<int:pk>/', views.update_user_data, name='update_user_data'),
    path('delete_user_data/<int:pk>/', views.delete_user_data, name='delete_user_data'),
    path('update_entry/<int:pk>/', views.update_entry, name='update_entry'),
    path('delete_entry/<int:pk>/', views.delete_entry, name='delete_entry'),
]