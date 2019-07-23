from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import ListViewSerializer, BookingSerializer
from datetime import date

class ListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = ListViewSerializer


class BookingView(ListAPIView):
	queryset = Booking.objects.filter(date__gte=date.today())
	serializer_class = BookingSerializer