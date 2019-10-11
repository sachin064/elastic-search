from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from elasticapp.documents import PostDocument


def search(request):
    q = request.GET.get('q')
    if q:
        posts = PostDocument.search().query("match", title=q)
    else:
        posts = ''
    return render(request, 'search/search.html', {'posts': posts})

