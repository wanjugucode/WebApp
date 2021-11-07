from django.urls import path
from .views import *
from stock import views




app_name='stock'
urlpatterns = [
   path('', views.home, name='home'),
   path('add_items/', views.add_items, name='add_items'),
   path('list_item/', views.list_item, name='list_item'),
   path('update_items/<str:pk>/', views.update_items, name="update_items"),
   
   path('view/',view_stock,name='stock_views'),
   path('add/',add_stock,name='add_stock'),
   path('edit/<int:id>/',edit_stock, name="edit_stock"),
   path('delete/<int:id>/',delete_stock, name="deleteStock"),

]
 
