from django.urls import path
from . import views

urlpatterns = [
    path('api/economic-events/', views.EconomicEventView.as_view(), name='economic-event-api'),
]
