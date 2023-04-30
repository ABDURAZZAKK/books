from django.urls import path
from .views import AuthorRegistrationAPI
  
author_urlpatterns = [
    path("", AuthorRegistrationAPI.as_view()),
]