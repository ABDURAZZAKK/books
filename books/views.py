from rest_framework import permissions, viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorPermission


class AllMethodsBooksAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorPermission)





