from django.contrib import admin
from .models import Restaurant, Table, Reservation, TimeSlot, Feedback

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(TimeSlot)
admin.site.register(Reservation)
admin.site.register(Feedback)
