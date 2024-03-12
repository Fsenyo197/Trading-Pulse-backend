from django.db import models

class EconomicEvent(models.Model):
    """
    Model representing an economic event.

    An economic event includes information such as currency, impact level,
    release date, event name, forecast, actual value, and outcome.

    The outcome is automatically determined based on the forecast and actual values.
    """
    IMPACT_CHOICES = (
        ('L', 'Low Impact'),
        ('M', 'Moderate Impact'),
        ('H', 'High Impact'),
    )
    currency = models.CharField(max_length=3, unique=False)
    impact_level = models.CharField(
        max_length=1,
        choices=IMPACT_CHOICES,
        null=True,
        blank=True
    )
    release_date = models.DateField()
    release_time = models.TimeField()
    event_name = models.CharField(max_length=100)
    previous = models.CharField(max_length=20, blank=True, null=True)
    forecast = models.CharField(max_length=20, blank=True, null=True)
    actual = models.CharField(max_length=20, blank=True, null=True)
    outcome = models.CharField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically determine the outcome based on forecast and actual values.

        This method automatically calculates the outcome of the economic event based on its forecast and actual values.
        If the forecast value is missing but the actual and previous values are present, it sets the forecast to 'neutral'.
        For special cases of economic events, the outcome logic is reversed compared to general cases.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None

        Raises:
            None
        """

        # List of special cases where the outcome logic is reversed
        special_cases = [
            "unemployment rate",
            "unemployment change",
            "Unemployment Claims",
            "claimant count change",
            "natural gas storage",
            "crude oil inventories",
            "prelim nonfarm productivity",
            "public sector net borrowing",
            "prelim wholesale inventories",
            "labor productivity",
        ]

        # Convert event name to lowercase for case-insensitive comparison
        event_name_lower = self.event_name.lower()

        # Determine outcome based on forecast and actual values
        if not self.forecast and self.actual and self.previous:
            self.outcome = 'neutral'
        elif any(special_case.lower() in event_name_lower for special_case in special_cases):
            if self.forecast and self.actual:
                forecast_value = self.convert_to_float(self.forecast)
                actual_value = self.convert_to_float(self.actual)
                if forecast_value is not None and actual_value is not None:
                    if forecast_value < actual_value:
                        self.outcome = 'negative'
                    elif forecast_value > actual_value:
                        self.outcome = 'positive' 
                    else:
                        self.outcome = 'neutral'
            else:
                self.outcome = None
        else:
            if self.forecast and self.actual:
                forecast_value = self.convert_to_float(self.forecast)
                actual_value = self.convert_to_float(self.actual)
                if forecast_value is not None and actual_value is not None:
                    if forecast_value < actual_value:
                        self.outcome = 'positive'
                    elif forecast_value > actual_value:
                        self.outcome = 'negative'
                    else:
                        self.outcome = 'neutral'
            else:
                self.outcome = None

        super().save(*args, **kwargs)



    def convert_to_float(self, value):
        """
        Convert a string value to float, handling 'K', 'M', 'B', and 'T' suffixes,
        and percentage values.
        """
        suffixes = {'K': 1000, 'M': 1000000, 'B': 1000000000, 'T': 1000000000000}
        try:
            if '%' in value:
                return float(value.strip('%')) / 100
            for suffix, factor in suffixes.items():
                if value.endswith(suffix):
                    return float(value[:-1]) * factor
            return float(value)
        except ValueError:
            return None


    def __str__(self):
        """
        Return a string representation of the economic event.
        """
        return f"{self.event_name} - {self.release_date} {self.release_time}"

    @classmethod
    def filter_events(cls, currency, impact_level):
        """
        Retrieve EconomicEvent instances filtered by currency and impact level.
        """
        if currency and impact_level:
            return cls.objects.filter(currency=currency, impact_level=impact_level, outcome__in=['positive', 'negative', 'neutral'])
        elif currency:
            return cls.objects.filter(currency=currency, outcome__in=['positive', 'negative', 'neutral'])
        elif impact_level:
            return cls.objects.filter(impact_level=impact_level, outcome__in=['positive', 'negative', 'neutral'])
        else:
            return cls.objects.filter(outcome__in=['positive', 'negative', 'neutral'])


'''

"""
Retrieve all EconomicEvent instances for a specific currency and its imapct level
"""
aud_low_impact_events = EconomicEvent.objects.filter(currency='AUD', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
aud_moderate_impact_events = EconomicEvent.objects.filter(currency='AUD', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
aud_high_impact_events = EconomicEvent.objects.filter(currency='AUD', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

cad_low_impact_events = EconomicEvent.objects.filter(currency='CAD', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
cad_moderate_impact_events = EconomicEvent.objects.filter(currency='CAD', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
cad_high_impact_events = EconomicEvent.objects.filter(currency='CAD', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

chf_low_impact_events = EconomicEvent.objects.filter(currency='CHF', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
chf_moderate_impact_events = EconomicEvent.objects.filter(currency='CHF', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
chf_high_impact_events = EconomicEvent.objects.filter(currency='CHF', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

cny_low_impact_events = EconomicEvent.objects.filter(currency='CNY', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
cny_moderate_impact_events = EconomicEvent.objects.filter(currency='CNY', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
cny_high_impact_events = EconomicEvent.objects.filter(currency='CNY', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

eur_low_impact_events = EconomicEvent.objects.filter(currency='EUR', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
eur_moderate_impact_events = EconomicEvent.objects.filter(currency='EUR', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
eur_high_impact_events = EconomicEvent.objects.filter(currency='EUR', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

gbp_low_impact_events = EconomicEvent.objects.filter(currency='GBP', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
gbp_moderate_impact_events = EconomicEvent.objects.filter(currency='GBP', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
gbp_high_impact_events = EconomicEvent.objects.filter(currency='GBP', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

jpy_low_impact_events = EconomicEvent.objects.filter(currency='JPY', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
jpy_moderate_impact_events = EconomicEvent.objects.filter(currency='JPY', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
jpy_high_impact_events = EconomicEvent.objects.filter(currency='JPY', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

nzd_low_impact_events = EconomicEvent.objects.filter(currency='NZD', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
nzd_moderate_impact_events = EconomicEvent.objects.filter(currency='NZD', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
nzd_high_impact_events = EconomicEvent.objects.filter(currency='NZD', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

usd_low_impact_events = EconomicEvent.objects.filter(currency='USD', impact_level='L', outcome__in=['positive', 'negative', 'neutral'])
usd_moderate_impact_events = EconomicEvent.objects.filter(currency='USD', impact_level='M', outcome__in=['positive', 'negative', 'neutral'])
usd_high_impact_events = EconomicEvent.objects.filter(currency='USD', impact_level='H', outcome__in=['positive', 'negative', 'neutral'])

'''
