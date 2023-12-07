from django.urls import path
from coursera_search.views import home, search_query

app_name = 'coursera_search'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_query, name='search_query'),
]