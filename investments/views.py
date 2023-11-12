from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Investment, Comentario, List
from .forms import InvestmentForm, ComentarioForm


class InvestmentListView(generic.ListView):
    model = Investment
    template_name = "investments/index.html"

def detail_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    context = {"investment": investment}
    return render(request, 'investments/detail.html', context)


def search_investments(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET["query"].lower()
        investment_list = Investment.objects.filter(name__icontains=search_term)
        context = {"investment_list": investment_list}
    return render(request, "investments/search.html", context)



def create_investment(request):
    if request.method == 'POST':
        investment_form = InvestmentForm(request.POST)
        if investment_form.is_valid():
            investment = Investment(**investment_form.cleaned_data)
            investment.save()
            return HttpResponseRedirect(reverse("investments:detail", args=(investment.pk,)))
    else:
        investment_form = InvestmentForm()
    context = {"investment_form": investment_form}
    return render(request, "investments/create.html", context)

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
            return HttpResponseRedirect(reverse("investments:detail", args=(investment_id,)))
    else:
        form = InvestmentForm(
            initial={
                "name": investment.name,
                "categoria": investment.categoria,
                "image_url": investment.image_url,
            }
        )
    context = {"investment": investment, "form": form}
    return render(request, "investments/update.html", context)


def delete_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)

    if request.method == "POST":
        investment.delete()
        return HttpResponseRedirect(reverse("investments:index"))

    context = {"investment": investment}
    return render(request, "investments/delete.html", context)


def create_comentario(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data["author"]
            review_text = form.cleaned_data["text"]
            review = Comentario(author=review_author, text=review_text, investment=investment)
            review.save()
            return HttpResponseRedirect(reverse("investments:detail", args=(investment_id,)))
    else:
        form = ComentarioForm()
    context = {"form": form, "investment": investment}
    return render(request, "investments/comentario.html", context)


class ListListView(generic.ListView):
    model = List
    template_name = "investments/lists.html"


class ListCreateView(generic.CreateView):
    model = List
    template_name = "investments/create_list.html"
    fields = ["name", "author", "investments"]
    success_url = reverse_lazy("investments:lists")
