from django.shortcuts import render, redirect
from .forms import SearchProviderForm
from utils.search_provider import seach_by_provider

def find_by_provider(request):
    if request.method == 'POST':
        form = SearchProviderForm(request.POST)
        if form.is_valid():
            searched_provider = form.cleaned_data['searched_provider']
            results = seach_by_provider(searched_provider)

            # Pass the modified data to the template
            return render(request, 'search_result.html', {'results': results})
    else:
        form = SearchProviderForm()

    return render(request, 'search_provider.html', {'form': form})