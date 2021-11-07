# from typing import FrozenSet
from django.shortcuts import render

# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .models import Product

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

# @login_required
# def index(request):
#     return render(request, 'dashboard/index.html')
# @login_required
# def product(request):
#     # items=Product.objects.all()
#     items=Product.object.raw('SELECT * FROM dashboard_products')

#     context={
#         'items':items,
#     }
#     return render(request, 'dashboard/product.html',context)


# @login_required
# def orders(request):
#     return render(request, 'dashboard/orders.html')