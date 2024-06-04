from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from datetime import datetime
from django.db.models import Q
from .models import EconomicEvent
from .serializers import EconomicEventSerializer
import logging

logger = logging.getLogger(__name__)

class EconomicEventView(APIView):
    def get(self, request, format=None) -> JsonResponse:
        # Retrieve query parameters
        currency = request.query_params.get('currency')
        impact_level = request.query_params.get('impact_level')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Convert date strings to datetime objects
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a cache key based on the query parameters
        cache_key = f"events_{currency}_{impact_level}_{start_date_str}_{end_date_str}"
        cached_events = cache.get(cache_key)
        
        if cached_events:
            return JsonResponse(cached_events, safe=False, status=status.HTTP_200_OK)

        # Initial filter: Only include events with the specified outcome
        events = EconomicEvent.objects.all()

        # Apply additional filters if parameters are provided
        if currency:
            events = events.filter(currency=currency)
        if impact_level:
            events = events.filter(impact_level=impact_level)
        if start_date:
            events = events.filter(release_date__gte=start_date)
        if end_date:
            events = events.filter(release_date__lte=end_date)
            
        # Logging: Print the filtered results to the console
        logger.debug(f"Filtered Events: {events}")

        # Serialize the queryset
        serializer = EconomicEventSerializer(events, many=True)

        # Cache the serialized data
        cache.set(cache_key, serializer.data, timeout=60*15)  # Cache for 15 minutes
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
