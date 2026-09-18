from django.urls import path
from .views import create_link, redirect_link

urlpatterns = [
   path("links/", create_link),
   path("<str:code>", redirect_link)
]