from django.urls import path
from question import views
from django.contrib import admin

urlpatterns = [
    path('', views.home),
    path('create', views.create, name = 'create'),
    path('show/', views.show),
    path('edit/<int:id>/', views.edit, name = 'edit'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
]