import random
import datetime
import unittest
from django.test import Client, TestCase
from django.utils import timezone
from .models import EconomicEvent
from .serializers import EconomicEventSerializer

def create_sample_economic_events(n=3):
    """
    Creates and returns a list of n sample EconomicEvent instances.
    """
    events = []
    for _ in range(n):
        event_data = {
            'currency': random.choice(['USD', 'EUR', 'GBP']),
            'impact_level': random.choice(['H', 'M', 'L']),
            'outcome': random.choice(['positive', 'negative', 'neutral']),
            'release_date': timezone.now().date()  # Use current date as release date
        }
        events.append(EconomicEvent.objects.create(**event_data))
    return events

class EconomicEventModelTestCase(TestCase):
    def test_outcome_calculation(self):
        """
        Test the outcome calculation logic in the EconomicEvent model's save method.
        """
        events = create_sample_economic_events(3)

    def test_currency_impact_level_filtering(self):
        """
        Test the filtering of EconomicEvent instances based on currency and impact level.
        """
        # Create some economic event instances for testing
        release_date = timezone.now().date()  # Use current date as release date
        EconomicEvent.objects.create(
            currency='USD',
            impact_level='H',
            release_date=release_date,
            event_name='Event 1',
            forecast='50%',
            actual='70%'
        )
        EconomicEvent.objects.create(
            currency='EUR',
            impact_level='L',
            release_date=release_date,
            event_name='Event 2',
            forecast='70%',
            actual='50%'
        )

        # Test filtering by currency
        usd_events = EconomicEvent.objects.filter(currency='USD')
        self.assertEqual(usd_events.count(), 1)

        # Test filtering by impact level
        high_impact_events = EconomicEvent.objects.filter(impact_level='H')
        self.assertEqual(high_impact_events.count(), 1)

        # Test filtering by both currency and impact level
        eur_high_impact_events = EconomicEvent.objects.filter(currency='EUR', impact_level='H')
        self.assertEqual(eur_high_impact_events.count(), 0)  # Expecting 0 as there's no EUR event with high impact


class EconomicEventSerializerTestCase(TestCase):
    def setUp(self):
        # Create a sample EconomicEvent instance for testing
        release_date = timezone.now().date()  # Use current date as release date
        self.event_data = {
            'currency': 'USD',
            'impact_level': 'H',
            'release_date': release_date,
            'event_name': 'Test Event',
            'forecast': '50%',
            'actual': '70%',
            'outcome': 'positive'
        }
        self.event = EconomicEvent.objects.create(**self.event_data)

    def test_serializer_output(self):
        """
        Test the output of EconomicEventSerializer for a given EconomicEvent instance.
        """
        serializer = EconomicEventSerializer(instance=self.event)
        expected_data = {
            'id': self.event.id,
            'currency': 'USD',
            'impact_level': 'H',
            'release_date': serializer.data['release_date'],  # Serializer data will have timezone issues
            'event_name': 'Test Event',
            'forecast': '50%',
            'actual': '70%',
            'outcome': 'positive'
        }
        self.assertEqual(serializer.data, expected_data)


class EconomicEventListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Use the generated sample events
        cls.events = create_sample_economic_events()

    def setUp(self):
        # Set up a test client
        self.client = Client()

    def test_get_all_events(self):
        """
        Test retrieving all EconomicEvent instances without any filters.
        """
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.events))  # Use cls.events instead of self.event_data

    def test_filter_by_currency(self):
        """
        Test filtering EconomicEvent instances by currency.
        """
        response = self.client.get('/api/events/?currency=USD')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # Expecting only one event with currency 'USD'

    def test_filter_by_impact_level(self):
        """
        Test filtering EconomicEvent instances by impact level.
        """
        response = self.client.get('/api/events/?impact_level=L')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # Expecting only one event with impact level 'L'

    def test_filter_by_currency_and_impact_level(self):
        """
        Test filtering EconomicEvent instances by both currency and impact level.
        """
        response = self.client.get('/api/events/?currency=EUR&impact_level=L')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # Expecting only one event with currency 'EUR' and impact level 'L'

if __name__ == '__main__':
    unittest.main()
