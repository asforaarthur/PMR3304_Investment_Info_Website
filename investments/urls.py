from django.urls import path

from . import views

app_name = "investments"
urlpatterns = [
    path('', views.InvestmentListView.as_view(), name='index'),
    path("search/", views.search_investments, name="search"),
    path("create/", views.create_investment, name="create"),
    path("<int:investment_id>/", views.detail_investment, name="detail"),
    path("update/<int:investment_id>/", views.update_investment, name="update"),
    path("delete/<int:investment_id>/", views.delete_investment, name="delete"),
    path("<int:investment_id>/comentario/", views.create_comentario, name="comentario"),
    path("lists/", views.ListListView.as_view(), name="lists"),
    path("lists/create", views.ListCreateView.as_view(), name="create-list"),
]
