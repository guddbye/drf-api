from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Stuff
from .permissions import IsOwnerOrReadOnly
from .serializers import StuffSerializer


class StuffList(ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
