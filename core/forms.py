from django import forms
from .models import Item

all_of_items = Item.objects.all()
Item_categories = []
for item in all_of_items:
    p = item.Item_Name
    Item_categories.append(p)

Itemz = ()
for item in Item_categories:
    p = (item, item),
    Itemz += p

print(Itemz)

print(Item_categories)
class Enquiry_Form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'class': 'form-control'
    }))
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={
        'placeholder' : '07123123123',
        'class': 'form-control'
    }))
    email = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'placeholder' : 'john@example.com',
        'class': 'form-control'
    }))
    item_enquiry = forms.ChoiceField(choices= Itemz)



