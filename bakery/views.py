from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

# developed by @raphaeltataia

from .models import Recipe

def post_list(request):
    recipes = Recipe.objects.order_by('created_date')
    return render(request, 'bakery/post_list.html', {'recipes': recipes})
