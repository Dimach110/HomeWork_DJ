from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorRetrive, MeasurementRetrive, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor', SensorView.as_view()),
    path('sensor/<pk>', SensorRetrive.as_view()),
    path('measurement', MeasurementView.as_view()),
    path('measurement/<pk>', MeasurementRetrive.as_view()),
    path('measurement/create', MeasurementCreate.as_view()),

]
