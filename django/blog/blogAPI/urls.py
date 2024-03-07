from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
    path('v1/articulos', BlogApi.as_view() )
]
