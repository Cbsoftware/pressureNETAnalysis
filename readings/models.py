from django.db import models


class Reading(models.Model):
    """Barometer reading from pressureNET"""
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_id = models.CharField(max_length=255, db_index=True)
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)
    altitude = models.FloatField(default=0.0)
    reading = models.FloatField()
    reading_accuracy = models.FloatField()
    provider = models.CharField(max_length=255, default='')
    observation_type = models.CharField(max_length=255, default='')
    observation_unit = models.CharField(max_length=255, default='')
    sharing = models.CharField(max_length=255)
    daterecorded = models.BigIntegerField(db_index=True)
    tzoffset = models.BigIntegerField()
    location_accuracy = models.FloatField()
    client_key = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'reading'
        verbose_name_plural = 'readings'
        unique_together = ('latitude', 'longitude', 'daterecorded', 'user_id')

    def __unicode__(self):
        return '%s: %s' % (self.user_id, self.reading)


class ReadingSync(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    readings = models.IntegerField()
    processing_time = models.FloatField()

    class Meta:
        verbose_name = 'reading sync'
        verbose_name_plural = 'reading syncs'

    def __unicode__(self):
        return '%s: %s' % (self.date, self.readings)
