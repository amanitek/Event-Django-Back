from rest_framework import serializers, viewsets
from .models import Event
from rest_framework.response import Response

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        # Handle event creation logic
        return super().create(request, *args, **kwargs)
