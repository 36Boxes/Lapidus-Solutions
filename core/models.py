from django.db import models

# Create your models here.

Item_Categories = (
    ('Soft Drink', 'Soft Drink'),
    ('Confectionery', 'Confectionery'),
    ('Fitness Food', 'Fitness Food')
)

class Item(models.Model):
    Item_Category = models.CharField(choices=Item_Categories, max_length=13)
    Item_Name = models.CharField(max_length=2000)
    Item_Picture = models.ImageField(upload_to='Product_Photos/', blank=True)
    Item_Description = models.TextField()
    Item_Price = models.DecimalField(decimal_places=2, max_digits=5)
    Item_Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.Item_Name



class Enquirie(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=11)
    customer_email = models.CharField(max_length=300)
    Item_enquiry = models.CharField(max_length=2000)
    Extra_Info = models.TextField(blank=True, null=True)
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.customer_first_name + ' ' + self.customer_last_name + ' ' + self.Item_enquiry + ' ' + self.customer_phone_number