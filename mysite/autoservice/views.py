from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
)

from .models import Paslauga, Paslaugos_kaina, AutomobilioModelis, Uzsakymas, UzsakymoEilute, Automobilis


# Create your views here.

def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(status__exact='a').count()
    automobiliu_kiekis = Automobilis.objects.all().count()

    # num_instances_available = BookInstance.objects.filter(status__exact='g').count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)


def uzsakymai(request):
    uzsakymai = Uzsakymas.objects.all()
    context = {
        'uzsakymai': uzsakymai
    }
    return render(request, 'uzsakymai.html', context=context)


def uzsakymas(request, uzsakymas_id):
    uzsakymas = get_object_or_404(Uzsakymas, pk=uzsakymas_id)
    return render(request, 'uzsakymas.html', {'uzsakymas': uzsakymas})

class AutomobiliaiView(ListView):
    model = Automobilis
    context_object_name = 'automobiliai'
    template_name = 'automobiliai.html'

class AutomobilisView(DetailView):
    model = Automobilis
    context_object_name = 'auto'
    template_name = 'automobilis.html'


from django.contrib.auth.mixins import LoginRequiredMixin


class UzsakymaiByUserListView(LoginRequiredMixin, ListView):
    model = Uzsakymas
    template_name = 'user_uzsakymai.html'

    def get_queryset(self):
        return Uzsakymas.objects.filter(klientas_id=self.request.user).order_by('grazinimo_laikas')

class UzsakymaiByUserDetailView(LoginRequiredMixin, DetailView):
    model = Uzsakymas
    template_name = 'user_uzsakymas.html'

class UzsakymaiByUserCreateView(LoginRequiredMixin, CreateView):
    model = Uzsakymas
    fields = ['automobilis_id', 'grazinimo_laikas']
    template_name = 'uzsakymas_form.html'

    def form_valid(self, form):
        form.instance.klientas_id = self.request.user
        return super().form_valid(form)

