from django.urls import path
from .views import new_order,order, send_order
app_name='orders'
urlpatterns = [
    path('new/',new_order,name='add_orders'),
    path("order/",order,name='order_views'),
    path('send/',send_order,name='send_order_views'),

]
