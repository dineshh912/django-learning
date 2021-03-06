from django.urls import path
from .views import CustomerCreateView, CustomerDetailView, CustomerView, CustomerEditView

urlpatterns = [
    path('add/', CustomerCreateView.as_view(), name="customer_add"),
    path('edit/<int:pk>/', CustomerEditView.as_view(), name="customer_edit"),
    path('<int:pk>/', CustomerDetailView.as_view(), name='list_view'),
    path('', CustomerView.as_view(), name='customer'),
   # path('bird_add/', BirdAddView.as_view(), name='add_bird' )
]
