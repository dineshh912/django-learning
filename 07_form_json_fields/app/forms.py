from django.forms import ModelForm, modelformset_factory, formset_factory
from .models import Bird, Customer
from django import forms
from entangled.forms import EntangledModelForm


BirdFormSet = modelformset_factory(
    Bird, fields=("common_name",  "scientific_name"), extra = 1, can_delete=True
)





class BirdForm(ModelForm):

    class Meta:
        model = Bird
        fields = ["common_name", "scientific_name"]



class testForm(EntangledModelForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.CharField(max_length=34, required=True)

    class Meta:
        model = Customer
        entangled_fields = {"text": ['name', 'email'] }
        untangled_fields = ['title']


testFormSet = formset_factory(testForm, extra=1)