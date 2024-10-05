from django.shortcuts import render, get_object_or_404, redirect
from .models import Search
from .forms import SearchForm, UpdateProductForm



def search_view(request):
    form = SearchForm(request.GET or None)
    query = ''
    results = []
    
    # Handle search request

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Search.objects.filter(name__icontains=query)

    return render(request, 'search/index.html', {'form': form, 'query': query, 'results': results})