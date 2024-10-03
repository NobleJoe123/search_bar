from django.shortcuts import render, get_object_or_404, redirect
from .models import Search
from .forms import SearchForm, UpdateProductForm



def search_view(request):
    form = SearchForm()
    results = None
    update_form = None
    product_to_update = None
    
    # Handle search request
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Search.objects.filter(name__icontains=query)

    # Handle update request
    if 'update_product_id' in request.POST:
        product_id = request.POST.get('update_product_id')
        product_to_update = get_object_or_404(Search, id=product_id)
        update_form = UpdateProductForm(request.POST, instance=product_to_update)
        
        if update_form.is_valid():
            update_form.save()
            return redirect('search_view')