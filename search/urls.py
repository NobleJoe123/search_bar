from django.urls import path
from .views import search_view, person_details
# search_create




urlpatterns = [
    path('', search_view, name='search'),
    path('details/', person_details, name='details'),

    
]
