from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, TemplateView
from .models import Customer, Bird
from django.shortcuts import redirect
from .forms import BirdFormSet, testForm
from django.http import QueryDict

# Create your views here.
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'add.html'
    fields = ('title', 'text')
    success_message = "added"
    success_url = reverse_lazy('view_address_type')

    def post(self, request):
        # super(Customer, self).post(request)
        title = request.POST['title']
        name = request.POST['name']
        email = request.POST['email']

        

        valid = {'title': title, 'text': {'name': name, 'email': email}}

        test = { "name": name, "email": email}
        
        form = testForm(valid or None)

        if form.is_valid():

            customer = Customer(title=title, text=test)
            customer.save()
  
            return redirect('customer')



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