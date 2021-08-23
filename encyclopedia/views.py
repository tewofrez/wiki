from re import search
from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    mkd = Markdown()
    entries = util.list_entries()
    if title in entries:
        page = util.get_entry(title)
        mkd_page = mkd.convert(page)

        content = {
            'page': mkd_page,
            'title': title
        }
        return render(request, "encyclopedia/entry.html", content)
    else:
        return render(request, "encyclopedia/error.html", {"display": "page not found!", "form": search()})
