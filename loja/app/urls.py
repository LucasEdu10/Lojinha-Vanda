from django.conf.urls import url
from django.conf import settings
from loja.app import views
from django.views.generic.base import RedirectView
from django.urls import include, path

urlpatterns = [
    path('', views.index),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.jpg')),
    path('home/', views.get_home),
    path('login/', views.get_login),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('contact/', views.get_contact),
    path('fabric/', views.get_fabric),
]