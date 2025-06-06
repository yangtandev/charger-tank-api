from rest_framework import generics
from .models import ChargerTankCurrent, ChargerTankHistory, ChargerTankStatus, ChargerTankStatusHistory
from .serializers import (
    ChargerTankCurrentSerializer,
    ChargerTankHistorySerializer,
    ChargerTankStatusSerializer,
    ChargerTankStatusHistorySerializer
)
from dateutil.parser import parse as parse_datetime
from datetime import timezone, timedelta

def parse_with_timezone(dt_str):
    try:
        dt = parse_datetime(dt_str)
        if dt.tzinfo is None:
            # 預設補上台灣時區 +08:00
            dt = dt.replace(tzinfo=timezone(timedelta(hours=8)))
        return dt
    except Exception as e:
        print(f"Failed to parse datetime: {e}")
        return None

class FilterableQuerysetMixin:
    date_field = 'record_datetime'  # default 時間欄位

    def get_queryset(self):
        queryset = super().get_queryset()
        temp_type = self.request.query_params.get('temp_type')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        count = self.request.query_params.get('count')
        order = self.request.query_params.get('order')

        if temp_type:
            queryset = queryset.filter(temp_type=temp_type)

        if start:
            start_dt = parse_with_timezone(start)
            if start_dt:
                queryset = queryset.filter(record_datetime__gte=start_dt)

        if end:
            end_dt = parse_with_timezone(end)
            if end_dt:
                queryset = queryset.filter(record_datetime__lt=end_dt)

        if order is not None:
            order = order.lower()
            if order == 'd':
                queryset = queryset.order_by(f'-{self.date_field}')
            elif order == 'a':
                queryset = queryset.order_by(f'{self.date_field}')

        if count is not None:
            try:
                count = int(count)
                queryset = queryset[:count]
            except ValueError:
                pass

        return queryset


# ChargerTankCurrent
class ChargerTankCurrentListCreateView(FilterableQuerysetMixin, generics.ListCreateAPIView):
    queryset = ChargerTankCurrent.objects.all()
    serializer_class = ChargerTankCurrentSerializer

class ChargerTankCurrentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerTankCurrent.objects.all()
    serializer_class = ChargerTankCurrentSerializer


# ChargerTankHistory
class ChargerTankHistoryListCreateView(FilterableQuerysetMixin, generics.ListCreateAPIView):
    queryset = ChargerTankHistory.objects.all()
    serializer_class = ChargerTankHistorySerializer

class ChargerTankHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerTankHistory.objects.all()
    serializer_class = ChargerTankHistorySerializer


# ChargerTankStatus
class ChargerTankStatusListCreateView(FilterableQuerysetMixin, generics.ListCreateAPIView):
    queryset = ChargerTankStatus.objects.all()
    serializer_class = ChargerTankStatusSerializer

class ChargerTankStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerTankStatus.objects.all()
    serializer_class = ChargerTankStatusSerializer

# ChargerTankStatusHistory
class ChargerTankStatusHistoryListCreateView(FilterableQuerysetMixin, generics.ListCreateAPIView):
    queryset = ChargerTankStatusHistory.objects.all()
    serializer_class = ChargerTankStatusHistorySerializer

class ChargerTankStatusHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerTankStatusHistory.objects.all()
    serializer_class = ChargerTankStatusHistorySerializer
