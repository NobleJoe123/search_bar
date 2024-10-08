from django.urls import path
from .views import search_view, search_update




urlpatterns = [
    path('search/', search_view, name='search'),

    
]
