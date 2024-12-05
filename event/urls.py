from django.contrib import admin
from django.urls import path

from event import views
from event.views import CustomTokenObtainPairView, user_logout

urlpatterns = [
    path('events/', views.get_events, name='get_events'),
    path('events/create/', views.create_event, name='create_event'),  # POST method for creating an event
    path('events/<int:event_id>/', views.update_event, name='update_event'),  # PUT method for updating an event
    path('events/<int:event_id>/', views.delete_event, name='delete_event'),  # DELETE method for deleting an event
]
