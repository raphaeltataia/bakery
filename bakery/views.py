from django.shortcuts import render

from django.http import HttpResponse

# developed by @raphaeltataia

def post_list(request):
    return render(request, 'bakery/post_list.html', {})
