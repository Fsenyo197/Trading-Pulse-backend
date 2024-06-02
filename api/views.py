from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EconomicEvent
from .serializers import EconomicEventSerializer
from datetime import datetime

class EconomicEventView(APIView):
    """
    API endpoint for retrieving filtered EconomicEvent instances.

    Accepts GET requests with query parameters for currency, impact level,
    start date, and end date to filter EconomicEvent instances and returns them as JSON.
    """

    def get(self, request, format=None):
        # Retrieve query parameters
        currency = request.query_params.get('currency')
        impact_level = request.query_params.get('impact_level')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Convert date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

        # Initial filter: Only include events with the specified outcome
        events = EconomicEvent.objects.filter(outcome__in=['positive', 'negative', 'neutral'])

        # Apply additional filters if parameters are provided
        if currency:
            events = events.filter(currency=currency)
        if impact_level:
            events = events.filter(impact_level=impact_level)
        if start_date:
            events = events.filter(release_date__gte=start_date)
        if end_date:
            events = events.filter(release_date__lte=end_date)

        # Debugging: Print the filtered results to the console
        print(f"Filtered Events: {events}")

        # Serialize and return the filtered events
        serializer = EconomicEventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
