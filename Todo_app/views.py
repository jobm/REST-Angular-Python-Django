from rest_framework import generics
from Todo_app.models import TodoItem
from Todo_app.serializer import TodoItemeSerializer


class TodotList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemeSerializer


class TodotItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemeSerializer