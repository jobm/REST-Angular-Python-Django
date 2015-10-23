from rest_framework import generics
from Todo_app.models import TodoItem
from Todo_app.serializer import TodoItemerializer


class TodotList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemerializer
