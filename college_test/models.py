from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} - {self.restaurant.name}"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} to {self.end_time}"


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.customer.username} - {self.restaurant.name}"


class Feedback(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Feedback by {self.reservation.customer.username}"
