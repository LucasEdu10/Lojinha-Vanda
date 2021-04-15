from django.conf.urls import url
from django.conf import settings
from loja.app import views
from django.views.generic.base import RedirectView
from django.urls import include, path

urlpatterns = [
    path('', views.get_home),
]