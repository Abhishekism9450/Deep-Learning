from django.shortcuts import render
from django.http import HttpResponse
from easytorch.models import Easy

def search_form(request):
    return render(request,'easytorch/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        value = Easy.objects.filter(type__icontains=q)
        return render(request, 'easytorch/search_results.html',
                      {'value': value, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
