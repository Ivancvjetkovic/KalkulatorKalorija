from django.forms import ModelForm
from .models import *


class dodajNamirnicuUTablicu(ModelForm):
    class Meta:
        model=RelacijaTablaNamirnica
        fields="__all__"
        
