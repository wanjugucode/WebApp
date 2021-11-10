from django import forms
from django.forms import fields
from django.forms.formsets import formset_factory
from .models import Menu, Stock
 
class AddStockForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields="__all__"


class DeleteStockForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields="__all__"
       
class StockCreateForm(forms.ModelForm):
    class Meta:
        model =Stock
        fields=['category','item_name','quantity'] # add fields in admin

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        return category


    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        
        for instance in Stock.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
        return item_name



class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required =False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['item_name','receive_quantity']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['item_name','receive_quantity']
        
class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model =Stock
        fields=['category','item_name','quantity',] 
        
        
class MenuForm(forms.ModelForm):
    class Meta:
        model =Menu
        fields=['item_name','quantity'] 

 
class AddMenu(forms.ModelForm):
   class Meta:
       model=Menu
       fields="__all__"
       
       
# class IssueMenuForm(forms.ModelForm):
# 	class Meta:
# 		model = Menu
# 		fields = ['item_name','quantity']
       
class MenuSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required =False)
    class Meta:
        model = Menu
        fields = [ 'item_name']







