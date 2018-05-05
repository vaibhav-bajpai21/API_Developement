from django.db import models

class Rooms(models.Model):
    """Represents the Rooms Price,Type"""
    room_id= models.AutoField(primary_key=True)
    price = models.IntegerField()
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type
        return self.room_id

class Room_Availability(models.Model):
    room_id= models.ForeignKey(Rooms)
    available=models.DateField(null=True)
