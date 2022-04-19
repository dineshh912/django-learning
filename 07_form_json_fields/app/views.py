from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, View, TemplateView
from .models import Customer, Bird
from django.shortcuts import redirect
from .forms import BirdFormSet, testForm, testFormSet
from django.shortcuts import render

# Create your views here.
class CustomerCreateView(View):
    model = Customer
    template_name = 'add.html'
    success_message = "added"
    form = testForm
    success_url = reverse_lazy('view_address_type')
    
    def get(self, request):

        return render(request, self.template_name, {'formset': testFormSet})

    def post(self, request):

        form = testFormSet(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
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