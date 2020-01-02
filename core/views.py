from django.shortcuts import render
from .models import Item, Enquirie
from  .forms import Enquiry_Form
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    new = Item.objects.order_by('-Item_Date')
    for count, item in enumerate(new):
        if count == 3:
            fourth_item = item
        if count == 2:
            third_item = item

        if count == 1:
            second_item = item
        if count == 0:

            first_new = item




    context = {
        '1item' : first_new,
        '2item' : second_item,
        '3item' : third_item,
        '4item' : fourth_item,
        'items' : new

    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def products(request):
    items = Item.objects.all()
    listop = [3,5,8,11,14,17]
    context = {
        'items' : items,
        'nums' : listop
    }
    return render(request, 'core/products.html', context)



class EnquiryView(View):
    def get(self, *args, **kwargs):
        form = Enquiry_Form()
        context = {
            'form' : form
        }
        return render(self.request, 'core/enquire.html', context)

    def post(self, *args, **kwargs):
        form = Enquiry_Form(self.request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            item_enquiry = form.cleaned_data.get('item_enquiry')
            extra_info = form.cleaned_data.get('extra_info')
            enquiry = Enquirie(
                customer_first_name=first_name,
                customer_last_name=last_name,
                customer_phone_number=phone,
                customer_email=phone,
                Item_enquiry=item_enquiry,
                Extra_Info=extra_info
            )
            enquiry.save()
            messages.warning(self.request, "Thank you for the enquiry we will get back to you as soon as we can!")
            return redirect('core:home')
        else:
            messages.warning(self.request, "Please fill out the enquiry form.")
            return redirect('enquiry')