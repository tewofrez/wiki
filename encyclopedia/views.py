from re import search
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Search Wiki', 'style': 'width:100%'}))


class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'myfieldclass', 'placeholder': 'Search'}))


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
            'title': title,
            'form': SearchForm()
        }
        return render(request, "encyclopedia/entry.html", content)
    else:
        return render(request, "encyclopedia/error_page.html", {"message": "The request page was not found", "form": search()})
