from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index_events", views.index_events, name='events')
]
