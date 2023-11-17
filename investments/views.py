import requests

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Investment, Comentario, List
from .forms import InvestmentForm, ComentarioForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def detail_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    if 'last_viewed' not in request.session:
        request.session['last_viewed'] = []
    request.session['last_viewed'] = [investment_id
                                      ] + request.session['last_viewed']
    if len(request.session['last_viewed']) > 5:
        request.session['last_viewed'] = request.session['last_viewed'][:-1]
    context = {'investment': investment}
    return render(request, 'investments/detail.html', context)

class InvestmentListView(generic.ListView):
    model = Investment
    template_name = 'investments/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            context['last_investments'] = []
            for investment_id in self.request.session['last_viewed']:
                context['last_investments'].append(
                    get_object_or_404(Investment, pk=investment_id))
        return context


def search_investments(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET["query"].lower()
        investment_list = Investment.objects.filter(name__icontains=search_term)
        context = {"investment_list": investment_list}
    return render(request, "investments/search.html", context)


@login_required
@permission_required('investments.add_investment')
def create_investment(request):
    if request.method == 'POST':
        investment_form = InvestmentForm(request.POST)
        if investment_form.is_valid():
            investment = Investment(**investment_form.cleaned_data)
            investment.save()
            return HttpResponseRedirect(
                reverse('investments:detail', args=(investment.pk, )))

    else:
        investment_form = InvestmentForm()
    context = {"investment_form": investment_form}
    return render(request, "investments/create.html", context)

@login_required
@permission_required('investments.update_investment')
def update_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment.name = form.cleaned_data["name"]
            investment.categoria = form.cleaned_data["categoria"]
            investment.image_url = form.cleaned_data["image_url"]
            investment.texto = form.cleaned_data["texto"]
            investment.save()
            return HttpResponseRedirect(reverse("investments:detail", args=(investment.id,)))
    else:
        form = InvestmentForm(
            initial={
                "name": investment.name,
                "categoria": investment.categoria,
                "image_url": investment.image_url,
                "texto": investment.texto,
            }
        )
    context = {"investment": investment, "form": form}
    return render(request, "investments/update.html", context)

@login_required
@permission_required('investments.delete_investment')
def delete_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)

    if request.method == "POST":
        investment.delete()
        return HttpResponseRedirect(reverse("investments:index"))

    context = {"investment": investment}
    return render(request, "investments/delete.html", context)

@login_required
def create_comentario(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_author = request.user
            comentario_text = form.cleaned_data["text"]
            comentario = Comentario(author=comentario_author, text=comentario_text, investment=investment)
            comentario.save()
            return HttpResponseRedirect(reverse("investments:detail", args=(investment_id,)))
    else:
        form = ComentarioForm()
    context = {"form": form, "investment": investment}
    return render(request, "investments/comentario.html", context)


class ListListView(generic.ListView):
    model = List
    template_name = "investments/lists.html"


class ListCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.CreateView):
    model = List
    template_name = 'investments/create_list.html'
    fields = ['name', 'author', 'investments']
    success_url = reverse_lazy('investments:lists')
    permission_required = 'investments.add_list'

def categorias(request):
    categorias = Investment.objects.values_list('categoria', flat=True).distinct()
    categorias_e_investimentos = {}
    
    for categoria in categorias:
        investimentos = Investment.objects.filter(categoria=categoria)
        categorias_e_investimentos[categoria] = investimentos

    return render(request, 'investments/categorias.html', {'categorias_e_investimentos': categorias_e_investimentos})

def posts_por_categoria(request, categoria):
    investimentos = Investment.objects.filter(categoria=categoria)
    return render(request, 'investments/posts_por_categoria.html', {'investimentos': investimentos, 'categoria': categoria})