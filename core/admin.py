from django.contrib import admin
from .models import Item, Enquirie

# Register your models here.
admin.site.site_header = "Lapidus Solutions Admin"
admin.site.site_title = "Lapidus Solutions Admin Portal"
admin.site.index_title = "Welcome to the Lapidus Solutions Admin Portal"
admin.site.register(Item)
admin.site.register(Enquirie)