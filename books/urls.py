from django.urls import path
from .views import AllMethodsBooksAPI
  
book_urlpatterns = [
    path("",  AllMethodsBooksAPI.as_view({'get':'list', 'post':'create'})),
    path("<int:pk>/",  AllMethodsBooksAPI.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]