from django.urls import path

from . import views

app_name = 'investments'
urlpatterns = [
    path('', views.list_investments, name='index'),
    path('search/', views.search_investments, name='search'),
    path('create/', views.create_investment, name='create'),
    path('<int:investment_id>/', views.detail_investment, name='detail'),
]
