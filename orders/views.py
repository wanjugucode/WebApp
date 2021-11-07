from django.shortcuts import render
from .models import  Order
from django.shortcuts import redirect, render
from .forms import OrderRegistrationForms
def new_order(request):
    if request.method=="POST":
      form=OrderRegistrationForms(request.POST,request.FILES)
      if form.is_valid():
            form.save()
      else:
            print(form.errors)
    else:
        form=OrderRegistrationForms()
    return  render(request,"new_order.html",{"form":form})
def order(request):
    orders=Order.objects.all()
    return render(request,"orders.html",{"orders":orders})

def send_order(request):
    return render(request,'send_email.html')