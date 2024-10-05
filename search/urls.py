from django.urls import path
from .views import search_view, search_update




urlpatterns = [
    path('search/', search_view, name='search'),
    path('update/<int:product_id>/', search_update, name='product_update'),

    
]
