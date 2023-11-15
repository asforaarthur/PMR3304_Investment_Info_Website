from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('staticpages.urls')),
    path('investments/', include('investments.urls')),
    path('accounts/', include('accounts.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
