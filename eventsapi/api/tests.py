from models import Event


# Create your tests here.
class TestModel():
    def test_model_events(self):
        event = Event(title="Coding with Python")
        assert "Coding with Python" is event.title
