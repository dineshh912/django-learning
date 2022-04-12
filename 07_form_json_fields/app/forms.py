from django.forms import ModelForm, modelformset_factory
from .models import Bird
from django import forms


BirdFormSet = modelformset_factory(
    Bird, fields=("common_name",  "scientific_name"), extra = 1, can_delete=True
)

COMMON_NAME_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class BirdForm(ModelForm):
    common_name = forms.ChoiceField(choices=COMMON_NAME_CHOICES)

    class Meta:
        model = Bird
        fields = ["common_name", "scientific_name"]