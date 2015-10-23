from rest_framework import serializers
from Todo_app.models import TodoItem

class TodoItemerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        field = ('id', 'item', 'description', 'created_at')
