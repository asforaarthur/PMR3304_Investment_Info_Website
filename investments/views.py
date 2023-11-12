from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import investment_data
from django.shortcuts import render


def detail_investment(request, investment_id):
    context = {'investment': investment_data[investment_id - 1]}
    return render(request, 'investments/detail.html', context)


def list_investments(request):
    context = {"investment_list": investment_data}
    return render(request, 'investments/index.html', context)


def search_investments(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "investment_list": [
                m for m in investment_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'investments/search.html', context)


def create_investment(request):
    if request.method == 'POST':
        investment_data.append({
            'name': request.POST['name'],
            'categoria': request.POST['categoria'],
            'image_url': request.POST['image_url']
        })
        return HttpResponseRedirect(
            reverse('investments:detail', args=(len(investment_data), )))
    else:
        return render(request, 'investments/create.html', {})
