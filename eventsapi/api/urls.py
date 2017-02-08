from django.conf.urls import url

from api.views import EventCreateAPIView, EventUpdateAPIView

urlpatterns = [
    url(r'^events/create/$', EventCreateAPIView.as_view(), name="events-create"),
    url(r'^events/update/(?P<pk>[0-9]+)$', EventUpdateAPIView.as_view(), name="events-update")
]
