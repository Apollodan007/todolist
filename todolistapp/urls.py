from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
    path('lists/<int:list_id>/add_item/', views.add_item, name='add_item')
]