from rest_framework import generics
from rest_framework.response import Response
from .models import Author
from .serializers import CreateAutorSerializer

class AuthorRegistrationAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all() 
    serializer_class = CreateAutorSerializer
