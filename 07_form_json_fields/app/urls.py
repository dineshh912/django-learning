from django.urls import path
from .views import CustomerCreateView, CustomerDetailView, CustomerView

urlpatterns = [
    path('add/', CustomerCreateView.as_view(), name="customer_add"),
    path('<int:pk>/', CustomerDetailView.as_view(), name='list_view'),
    path('', CustomerView.as_view(), name='customer')
]
