from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Person, BankDetail
from .forms import SearchForm, CreateForm, DetailForm



def search_view(request):
    search_form = SearchForm(request.GET or None)
    create_form = CreateForm(request.POST, request.FILES)
    people = Person.objects.all()[:10]
    query = ''
    results = []
    
    # Handle search request

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        results = Person.objects.filter(name__icontains=query)

    if request.method == 'POST' and create_form.is_valid():
        create_form.save()
        return redirect('search')  # Redirect after saving

    return render(request, 'search/index.html', {
        'search_form': search_form,
        'create_form': create_form, 
        'people': people,
        'query': query, 
        'results': results
       
    })



def person_details(request):
     person_id = request.GET.get('id')  # Get the person ID from the URL
     person = get_object_or_404(Person, id=person_id)  # Fetch the person from the database
     banks = BankDetail.objects.filter(person=person)
     detail_form = DetailForm(request.POST)
     
     if request.method == 'POST' and detail_form.is_valid():
        detail_form.save()
        return redirect('search')  # Redirect after saving

     
     return render(request, 'search/details.html', {
    'person' : person,
    'banks': banks,
    'detail_form': detail_form
        
    })

# def bank_details(request, person_id):

#     person = get_object_or_404(Person, id=person_id)
    

#     return render(request, 'search/details.html',{
#         'person': person, 
#         'banks':banks
        
#         })





















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
