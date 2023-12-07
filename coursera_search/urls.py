from django.urls import path
from .views import find_by_provider

app_name = 'example_app'

urlpatterns = [
    path('by-provider/', find_by_provider, name='search_provider'),
    path('result/', find_by_provider, name='search_result'),
]