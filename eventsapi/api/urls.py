from django.conf.urls import url

from api.views import EventCreateAPIView, EventUpdateAPIView, EventDeleteAPIView

urlpatterns = [
    url(r'^events/create/$', EventCreateAPIView.as_view(), name="events-create"),
    url(r'^events/update/(?P<pk>[0-9]+)$', EventUpdateAPIView.as_view(), name="events-update"),
    url(r'^events/delete/(?P<pk>[0-9]+)$', EventDeleteAPIView.as_view(), name="events-delete")
]
