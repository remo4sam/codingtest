from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from models import Event


# Create your tests here.
class TestModel():
    def test_model_events(self):
        event = Event(title="Coding with Python")
        assert "Coding with Python" is event.title


class TestEventCreateApiView(APITestCase):
    def test_creation_of_event(self):
        url = reverse('api:events-create')
        data = {"title": "coding in python"}
        response = self.client.post(url, data)
        assert response.status_code == 201
        assert Event.objects.all().count() == 1
