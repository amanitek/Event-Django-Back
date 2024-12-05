from django.http import JsonResponse
from django.shortcuts import render

from event.serializer import EventSerializer

from .models import Event
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from tutorial.quickstart.serializers import UserSerializer
from django.contrib.auth import logout



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(email=request.data['email'])
            response.data['isAdmin'] = user.is_staff  # Add custom field
        return response

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_logout(request):
    logout(request) 
    return JsonResponse({'message': 'Logged out successfully'})

@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Event created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all events
@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()  # Fetch all events from the database
    serializer = EventSerializer(events, many=True)  # Serialize the event data
    return Response(serializer.data)  

# Update an event
@api_view(['PUT'])
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Event updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete an event
@api_view(['DELETE'])
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        event.delete()
        return Response({'message': 'Event deleted successfully'}, status=status.HTTP_200_OK)