from django.db import models

# Create your models here.
class Booking(models.Model):
    ROOM_CHOICES = [
        ("003", "003"),
        ("008", "008"),
        ("105", "105"),
        ("203", "203"),
        ("701", "701"),
        ("703", "703"),
        ("Board Room", "Board Room"),
        # Add more choices as needed
    ]
    room = models.CharField(max_length=10, choices=ROOM_CHOICES)
    time = models.CharField(max_length=10)
    committee = models.CharField(max_length=100)
    reason = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.room}-{self.committee}-{self.time}-{self.date}"

