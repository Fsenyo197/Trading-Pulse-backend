import os
import django
import csv

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Now you can import your models
from .models import EconomicEvent
from datetime import datetime

def import_economic_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            currency = row['Currency']
            impact_level = row['Impact']

            # Parse date and time separately
            release_date_str = row['Date']
            release_time_str = row['Time']

            # Parse date
            release_date = datetime.strptime(release_date_str, '%m/%d/%Y').date()

            # Parse time without seconds
            release_time = datetime.strptime(release_time_str, '%H:%M').time()

            event_name = row['Event']
            previous = row['Previous']
            forecast = row['Forecast']
            actual = row['Actual']
            outcome = row['Outcome']

            # Create and save EconomicEvent instance
            event = EconomicEvent.objects.create(
                currency=currency,
                impact_level=impact_level,
                release_date=release_date,
                release_time=release_time,
                event_name=event_name,
                previous=previous,
                forecast=forecast,
                actual=actual,
                outcome=outcome
            )
