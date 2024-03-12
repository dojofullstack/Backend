from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
    path('v1/articulos', BlogApi.as_view() ),
    path('v1/articulo/create', BlogApi.as_view() ),
    path('v1/articulo/<slug:id>', BlogApi.as_view() )
]
