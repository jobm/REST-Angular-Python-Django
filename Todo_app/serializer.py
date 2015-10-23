from rest_framework import serializers
from Todo_app.models import TodoItem

class TodoItemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        field = ('id', 'item', 'description', 'created_at')
