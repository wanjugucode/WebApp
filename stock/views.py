import csv
from django.http import request
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponse 





 
# Create your views here.
def stock(request):
   return render(request,'stock.html',{})
 

def add_stock(request):
   if request.method=='POST':
       form=AddStockForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           messages.success(request, 'Successfully Saved')
       else:
           print(form.errors)
   else:
       form=AddStockForm()
   return render(request,"add_stock.html",{"form":form})
 
def view_stock(request):
   stock=Stock.objects.all()
   return render(request,"stock.html",{ 'stock':stock})
 
 
def edit_stock(request,id): 
    stock=Stock.objects.get(id=id)
    if request.method=="POST":
        form=AddStockForm(request.POST,request.FILES,instance=stock)
        if form.is_valid():
            form.save()      
    else:
        form=AddStockForm(instance=stock)
    return render(request,'edit_stock.html',{"form":form})
def delete_stock(request,id):
    try:
        stock=Stock.objects.get(id=id)
        stock.delete()
    except Stock.DoesNotExist:
        stock=None
    return render(request,"stock.html",{})


def home(request):
    title='Welcome:Stock management'
    form="welcome"
    context={
        "title":title,
        "test":form
       
    }
    return render (request,'home.html',context)

def list_item(request):
    header='Stock'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form":form
    }
    
    if request.method == 'POST':
        queryset = Stock.objects.filter(
            # category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
            )
     
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

        context = {
            "form": form,
            "header": 'header',
            "queryset": queryset,
                  }
    return render(request, "list_item.html", context)

def add_items(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/stock/list_item')
    context={
        "form":form,
        "title":'Additems',
        }
    return render(request,"add_items.html",context)
    

def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/stock/list_item')
    context = {
        'form':form
	}
    return render(request, 'add_items.html', context)

