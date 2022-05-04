from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, View, TemplateView
from .models import Customer, Bird
from django.shortcuts import redirect
from .forms import BirdFormSet, CustomerForm, customerFormset
from django.shortcuts import render

# Create your views here.
class CustomerCreateView(View):
    model = Customer
    template_name = 'add.html'
    success_message = "added"
    customer_form = CustomerForm()
    address_form = customerFormset()
    success_url = reverse_lazy('view_address_type')
    
    def get(self, request):

        return render(request, self.template_name, 
            {'customer_form': self.customer_form,
             'address_form': self.address_form})

    def post(self, request):

        customer_data = CustomerForm(request.POST)
        address_data = customerFormset(request.POST)

        if customer_data.is_valid() and address_data.is_valid():
            print(customer_data.cleaned_data)
            print(address_data.cleaned_data)
        else:
            print("invalid")




class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'view.html'


class CustomerView(TemplateView):
    template_name = 'all.html'


class BirdAddView(TemplateView):
    template_name = 'add_bird.html'

    def get(self, *args, **kwargs):

        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})

    def post(self, *args, **kwargs):
        
        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
            pass
            # formset.save()
            # return redirect(reverse_lazy("customer"))
        
        return self.render_to_response({'bird_formset': formset})