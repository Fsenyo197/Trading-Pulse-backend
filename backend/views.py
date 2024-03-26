from api.models import EconomicEvent
from api.serializers import EconomicEventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def root_route(request):
    if request.method == 'GET':
        events = EconomicEvent.objects.all()  # Retrieve all records from the database
        serializer = EconomicEventSerializer(events, many=True)  # Serialize the queryset
        return Response(serializer.data)

