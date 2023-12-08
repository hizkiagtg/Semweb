from django.urls import path
from coursera_search.views import home, search_query, get_search_results

app_name = 'coursera_search'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_query, name='search_query'),
    path('query/<str:search_by>/<str:query>/', get_search_results, name='get_search_results'),
]