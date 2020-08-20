from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TrafficLog(models.Model):
    user_id = models.IntegerField(verbose_name='user_id')
    traffic_mb = models.IntegerField(verbose_name='traffic', default=0)
    created_at = models.DateTimeField(
        verbose_name='Datetime', 
        auto_created=True,
        auto_now_add=True
    )

    def __str__(self):
        return f'User {self.user_id}, trffic {self.traffic_mb} Mb, date {self.created_at}'

    class Meta:
        verbose_name='Traffic entry'
