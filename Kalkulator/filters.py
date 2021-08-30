import django_filters
from .models import *

class filterNamirnicaDB(django_filters.FilterSet):
    class Meta:
        model = Namirnica
        fields = ['naziv']  