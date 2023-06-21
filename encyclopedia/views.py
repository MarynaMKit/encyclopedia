from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    if util.get_entry(name) == None:
        return HttpResponse(f"We don't have article '{name}' in our encyclopedia")
    else:
        return render(request, "encyclopedia/article.html", {
        "articles": markdown.markdown(util.get_entry(name))
    })

# def test(request, name):
#      return HttpResponse(f"article - {name}")

# def test (request, name):
#     return render(request, "encyclopedia/article.html", {
#         "articles": markdown.markdown(util.get_entry(name))
#     })