# Create your views here.
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from api.models import Event
from api.serializers import EventCreateSerializer


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer


class EventUpdateAPIView(UpdateAPIView):
    serializer_class = EventCreateSerializer

    def get_queryset(self):
        return Event.objects.filter(pk=self.kwargs.get('pk'))


class EventDeleteAPIView(DestroyAPIView):
    def get_queryset(self):
        return Event.objects.filter(pk=self.kwargs.get('pk'))
