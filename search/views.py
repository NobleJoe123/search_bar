from django.shortcuts import render
from .models import Search
from .forms import SearchForm



def search_view(request):
    form = SearchForm(request.GET or None)
    query = ''
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Search.objects.filter(name__icontains=query)

    return render(request, 'search/index.html', {'form': form, 'query': query, 'results': results})
