from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, View, TemplateView
from .models import Customer, Bird
from django.shortcuts import redirect
from .forms import CustomerForm, AddressFormset
from django.shortcuts import render

# Create your views here.
class CustomerCreateView(View):
    model = Customer
    template_name = 'add.html'
    success_message = "added"

    customer_form = CustomerForm()
    address_form = AddressFormset()
    # contact_form = ContactFormset()
    
    def get(self, request):

        return render(request, self.template_name, 
            {'customer_form': self.customer_form,
             'address_form': self.address_form})

    def post(self, request):

        customer_data = CustomerForm(request.POST)
        address_data = AddressFormset(request.POST)
        customer_address = {}
        customer_contact = {}
        if customer_data.is_valid() and address_data.is_valid():
            for i in address_data.cleaned_data:
                customer_address[i['address']['address']] = i['address']
                customer_contact[i['contact']['phone']] = i['contact']
            obj = Customer()
            obj.name = customer_data.cleaned_data.get("name")
            obj.address = customer_address
            obj.contact = customer_contact
            obj.save()
            print("i am saved")         
        else:
            print("invalid")


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'view.html'


class CustomerView(TemplateView):
    template_name = 'all.html'



# class BirdAddView(TemplateView):
#     template_name = 'add_bird.html'

#     def get(self, *args, **kwargs):

#         formset = BirdFormSet(queryset=Bird.objects.none())
#         return self.render_to_response({'bird_formset': formset})

#     def post(self, *args, **kwargs):
        
#         formset = BirdFormSet(data=self.request.POST)

#         if formset.is_valid():
#             pass
#             # formset.save()
#             # return redirect(reverse_lazy("customer"))
        
#         return self.render_to_response({'bird_formset': formset})