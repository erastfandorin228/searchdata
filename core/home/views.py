from platform import system

from django.shortcuts import render


def get_alco():
    return ["Jim Beam", "Vodka", "Pivo"]


def index(request):
    return render(request, "index.html", {"alco": get_alco(), "title": "Main"})


def index_events(request):
    return render(request, "index_events.html")

def thank_you(request):
    return render(request, "thank_you.html")
