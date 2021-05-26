from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=500)
    
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, 
        blank=False,
    )

    interval = models.IntegerField(
        default=10,
        help_text="Interval of checking in seconds"
    )

    is_paused = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
