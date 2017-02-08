from django.conf.urls import url

from api.views import EventCreateAPIView

urlpatterns = [
    url(r'^events/create/$', EventCreateAPIView.as_view(), name="events-create")
]
