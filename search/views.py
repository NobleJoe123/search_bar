from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import BioData
from .forms import SearchForm, CreateForm



def search_view(request):
    search_form = SearchForm(request.GET or None)
    create_form = CreateForm(request.POST or None)
    query = ''
    results = []
    
    # Handle search request

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        results = BioData.objects.filter(name__icontains=query)

    if request.method == 'POST' and create_form.is_valid():
        create_form.save()
        return redirect('search')  # Redirect after saving

    return render(request, 'search/index.html', {
        'search_form': search_form,
        'create_form': create_form,
        'query': query, 
        'results': results
    })



def person_view(request):
    # Get the first 10 records from the Person table
    people = BioData.objects.all()[:10]
    
    return render(request, 'search/index.html', {
        'people': people
    })





















# def search_update(request, pk):

#     # product = get_object_or_404(Search, id=product_id)
#     if request.method == 'POST':
#         form = CreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('search_create')  # Redirect back to the search page
#     else:
#         form = CreateForm()
#         return render(request, 'search/main.html', {'form':form})





# def update_todo(request, pk):
#     todo = Todo.objects.get(id=pk)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'mood/update_todo.html', {'form': form}





# def search_view(request):
#     form = SearchForm(request.GET or None)
#     query = ''
#     results = []
    
#     # Handle search request

#     if form.is_valid():
#         query = form.cleaned_data.get('query')
#         results = Search.objects.filter(name__icontains=query)

#     return render(request, 'search/index.html', {'form': form, 'query': query, 'results': results})



# def search_create(request):
#     # product = get_object_or_404(Search, id=product_id)
#     if request.method == 'POST':
#         form = CreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('search_create')  # Redirect back to the search page
#     else:
#         form = CreateForm()
#         return render(request, 'search/main.html', {'form':form})
