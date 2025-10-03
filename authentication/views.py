from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Country
from .forms import CountryForm
def country_list(request):
    countries = Country.objects.all().order_by('name')
    return render(request, 'authentication_app/country_list.html', {'countries': countries})  # ← CAMBIADO

def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('authentication_app:country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'authentication_app/country_form.html', {'form': form, 'country': country})
