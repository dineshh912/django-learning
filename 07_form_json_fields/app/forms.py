from django.forms import ModelForm, modelformset_factory
from .models import Bird


BirdFormSet = modelformset_factory(
    Bird, fields=("common_name",  "scientific_name"), extra = 1, can_delete=True
)

class BirdForm(ModelForm):

    class Meta:
        model = Bird
        fields = ["common_name", "scientific_name"]