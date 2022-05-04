from django.forms import ModelForm, modelformset_factory, formset_factory
from .models import Bird, Customer
from django import forms
from entangled.forms import EntangledModelForm


class BirdForm(ModelForm):

    class Meta:
        model = Bird
        fields = ["common_name", "scientific_name"]


BirdFormSet = modelformset_factory(
    Bird, fields=("common_name",  "scientific_name"), extra = 1, can_delete=True
)

# class testForm(EntangledModelForm):
#     name = forms.CharField(max_length=255, required=True)
#     email = forms.CharField(max_length=34, required=True)

#     class Meta:
#         model = Customer
#         entangled_fields = {"text": ['name', 'email'] }
#         untangled_fields = ['title']


# testFormSet = formset_factory(testForm, fields=('name', 'email'),extra=1)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name"]


class AddressForm(EntangledModelForm):
    address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=255, required=True)
    country = forms.CharField(max_length=255, required=True)

    phone = forms.CharField(max_length=255, required=True)
    email = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Customer
        entangled_fields = {"address": ['address', "city", "country"],
                            "contact": ['phone', 'email']}


class ContactForm(EntangledModelForm):

    phone = forms.CharField(max_length=255, required=True)
    email = forms.CharField(max_length=255, required=True)
    
    class Meta:
        model = Customer
        entangled_fields = {"contact": ['phone', "email"] }


AddressFormset = formset_factory(AddressForm, extra=1)

# ContactFormset = formset_factory(ContactForm, extra=1)
