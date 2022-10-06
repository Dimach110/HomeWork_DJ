# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializers, SensorDetailSerializer


# class SensorView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#     def post(self, request):
#         # testData = {'response': 'ok-post'}
#         return Response(testData)
#
#     def patch(self, request):
#         testData = {'response': 'ok-patch'}
#         return Response(testData)

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class SensorRetrive(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementRetrive(RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer