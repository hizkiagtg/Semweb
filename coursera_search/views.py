from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse
from coursera_search.utils import RDFHandle
from functools import lru_cache
from coursera_search.forms import SearchForm

def home(request):
    form = SearchForm()
    return render(request, 'index.html', {'form': form})

@lru_cache(maxsize=None)  
def query_rdf(search_by, query):
    rdf = RDFHandle()
    return rdf.search(search_by, query)

def search_query(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['sms_text']
            search_by= form.cleaned_data['search_type']
            results = query_rdf(search_by, query)
            context = {
                'results': results,
                'form': form
            }
            return render(request, 'index.html', context)
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

def get_search_results(request, search_by, query):
    if request.method == 'GET':
        results = query_rdf(search_by, query)
        return JsonResponse(results, safe=False)
    return JsonResponse({"success": False}, status=400)
