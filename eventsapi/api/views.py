# Create your views here.
from rest_framework.generics import CreateAPIView

from api.serializers import EventCreateSerializer


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
