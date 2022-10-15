from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название датчика')
    description = models.CharField(max_length=128, verbose_name='Описание датчика')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название датчика'
        verbose_name_plural = 'Названия датчиков'

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temp = models.IntegerField(verbose_name='Значение температуры')
    date = models.DateTimeField(auto_now=True, verbose_name='дата измерения')


    def __str__(self):
        return self.temp

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ('sensor_id',)

