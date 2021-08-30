from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from .filters import filterNamirnicaDB
# Create your views here.

#@login_required(login_url='login')
#@admin_only
def home(request):
    listaSvihNamirnica=Namirnica.objects.filter()
    myfilter = filterNamirnicaDB(request.GET,queryset=listaSvihNamirnica)
    listaSvihNamirnica=myfilter.qs
    total=RelacijaTablaNamirnica.objects.all()
    myfooditems=total.filter(tablica=1)
    print(myfooditems)

    ukupanBrojNamirnica = myfooditems.count()

    querysetFood=[]
    for food in myfooditems:
        querysetFood.append(food.namirnica.all())


    trenutnaListaNamirnica=[]
    for items in querysetFood:
        for food_items in items:
            trenutnaListaNamirnica.append(food_items)

    #zbrajamo ukupan zbir kalorija, uh-a, masnoce i proteina
    ukupnoKalorija = 0
    ukupnoUgljikohidrata = 0
    ukupnoMasnoce = 0
    ukupnoProteina = 0
    for foods in trenutnaListaNamirnica:
        ukupnoKalorija += foods.kalorije
        ukupnoUgljikohidrata += foods.ugljikohidrati
        ukupnoMasnoce += foods.masnoca
        ukupnoProteina += foods.proteini
    
    context={'ukupnoProteina':ukupnoProteina, 'ukupnoMasnoce':ukupnoMasnoce, 'ukupnoUgljikohidrata':ukupnoUgljikohidrata,'ukupnoKalorija':ukupnoKalorija,'ukupanBrojNamirnica':ukupanBrojNamirnica,'trenutnaListaNamirnica':trenutnaListaNamirnica,'listaSvihNamirnica':listaSvihNamirnica}
    return render(request,'kalkulator.html',context)


def dodajNamirnicu(request):
    
    if request.method=="POST":
        form = dodajNamirnicuUTablicu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=dodajNamirnicuUTablicu()
    context={'form':form}
    return render(request,'dodajNamirnicu.html',context)

