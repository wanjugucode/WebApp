from django.urls import path
from .views import menu
app_name='menu'
urlpatterns = [
    path('',menu,name='menu_views'),
]
