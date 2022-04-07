from django.views.generic import DetailView, CreateView, TemplateView
from .models import Customer
from django.shortcuts import redirect

# Create your views here.
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'add.html'
    fields = ('title', 'text')

    def post(self, request):
        # super(Customer, self).post(request)
        title = request.POST['title']
        name = request.POST['name']
        email = request.POST['email']

        test = { "name": name, "email": email}

        customer = Customer(title=title, text=test)
        customer.save()
  
        return redirect('customer')



class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'view.html'


class CustomerView(TemplateView):
    template_name = 'all.html'