from django.db import models

# Create your models here.

class RoomType(models.Model):

    room_id = models.IntegerField("room_id", primary_key=True)
    room_type = models.CharField("room_type", max_length = 30, null= False)

    def __str__(self):
        return self.room_type



class Location(models.Model):

    location_id = models.IntegerField("location_id", primary_key=True)
    location_name = models.CharField("location_name", max_length = 100, null= False)

    def __str__(self):
        return self.room_type


class Arena(models.Model):
    branch_id = models.IntegerField("branch_id", primary_key=True)

    

class Booking(models.Model):
    booking_id = models.IntegerField("booking_id", primary_key = True, null= False)
    seat_no = models.IntegerField("seat_no", null= False)
    from_date = models.DateTimeField("from_date")
    to_data = models.DateTimeField("to_data")
    from_time = models.TimeField("from_time")
    to_time = models.TimeField("to_time")
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE,)
    branch_id = models.ForeignKey( 'Arena', on_delete=models.CASCADE)


