from django.test import TestCase
from .utils import import_economic_data_from_csv
from .models import EconomicEvent

class EconomicDataImportTestCase(TestCase):
    def test_import_from_csv(self):
        # Path to your CSV file
        csv_file_path = '/path/to/your/csv/file.csv'

        # Call the import function
        import_economic_data_from_csv(csv_file_path)

        # Add assertions to verify data import
        # For example:
        self.assertEqual(EconomicEvent.objects.count(), expected_count)
        # Add more assertions as needed