from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect

from django.shortcuts import render, redirect
from datetime import datetime
from django.template.loader import render_to_string
from django.urls import reverse

def index(request):
    # t = render_to_string("woman/index.html")
    # return HttpResponse(t)
    return render(request, "woman/index.html")

def about(request):
    return render(request, "woman/about.html")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        res = []
        for key, value in request.GET.items():
            res.append(f"{key}={value}")
        return HttpResponse("|".join(res))
    else:
        return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > datetime.now().year:
        uri = reverse(categories_by_slug, args=("music", ))
        return redirect(uri)
        # return HttpResponsePermanentRedirect(uri)
    else:
        return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")