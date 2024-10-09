from django.urls import path
from .views import search_view
# search_create




urlpatterns = [
    path('', search_view, name='search'),
    # path('search/', search_create, name='search_create'),

    
]
