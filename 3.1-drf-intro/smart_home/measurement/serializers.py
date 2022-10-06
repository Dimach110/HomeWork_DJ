from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


# Ручное описание сериалазера
# class SensorSerializer(serializers.Serializer):
    # name = serializers.CharField
    # description = serializers.CharField

# class MeasurementSerializer(serializers.Serializer):
    # id = serializers.IntegerField
    # temp = serializers.IntegerField
    # date = serializers.IntegerField

# Упрощённое задание сериалайзера
class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temp']

#Используем вложенный Сериализатор
# (https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects)
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


