from django.urls import path
from . import views
from .views import EnquiryView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('enquiry/', EnquiryView.as_view(), name='enquiry'),
]