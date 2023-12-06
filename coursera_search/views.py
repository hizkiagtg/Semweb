from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def home(request):
	return render(request, 'index.html')