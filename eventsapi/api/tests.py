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


class TestEventUpdateApiView(APITestCase):
    def test_update_of_event(self):
        event = Event.objects.create(title='Wrong title')
        url = reverse('api:events-update', kwargs={'pk': event.id})
        data = {"title": "new correct title"}
        response = self.client.put(url, data)
        assert response.status_code == 200
        assert event.title == 'Wrong title'
        new_event = Event.objects.get(pk=event.id)
        assert new_event.title == 'new correct title'


class TestEventDeleteApiView(APITestCase):
    def test_event_of_event(self):
        event = Event.objects.create(title='Wrong title')
        url = reverse('api:events-delete', kwargs={'pk': event.id})
        assert Event.objects.all().count() == 1
        response = self.client.delete(url)
        assert response.status_code == 204
        assert Event.objects.all().count() == 0



class TestSubscribeApiView(APITestCase):
    def test_subscribe_to_an_event(self):
        event = Event.objects.create(title='Wrong title')
        url = reverse('api:events-subscribe', kwargs={'pk': event.id})
        response = self.client.delete(url)
        assert response.status_code == 204
        assert Event.objects.all().count() == 0