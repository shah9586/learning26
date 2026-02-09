from .models import Reservation, Table


class ReservationService:

    @staticmethod
    def check_table_availability(restaurant, date, slot):
        booked_tables = Reservation.objects.filter(
            restaurant=restaurant,
            date=date,
            slot=slot,
            status='Confirmed'
        ).values_list('table_id', flat=True)

        return Table.objects.exclude(id__in=booked_tables)


    @staticmethod
    def confirm_reservation(reservation):
        reservation.status = 'Confirmed'
        reservation.save()
