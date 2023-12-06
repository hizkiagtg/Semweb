from django.urls import path
from coursera_search.views import home

app_name = 'coursera_search'

urlpatterns = [
    path('home/', home, name='home'),
]