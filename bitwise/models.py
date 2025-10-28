from django.db import models

class Entry(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    average = models.FloatField()
    positive_count = models.IntegerField()
    even_odd = models.JSONField()
    sorted_values = models.JSONField()
    warning = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)