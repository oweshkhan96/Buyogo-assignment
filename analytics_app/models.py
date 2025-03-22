from django.db import models

class Booking(models.Model):
    hotel = models.CharField(max_length=100)
    is_canceled = models.IntegerField()
    lead_time = models.IntegerField()
    arrival_date_year = models.IntegerField()
    arrival_date_month = models.CharField(max_length=20)
    arrival_date_week_number = models.IntegerField()
    arrival_date_day_of_month = models.IntegerField()
    stays_in_weekend_nights = models.IntegerField()
    stays_in_week_nights = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    babies = models.IntegerField()
    meal = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    market_segment = models.CharField(max_length=50)
    distribution_channel = models.CharField(max_length=50)
    is_repeated_guest = models.IntegerField()
    previous_cancellations = models.IntegerField()
    previous_bookings_not_canceled = models.IntegerField()
    reserved_room_type = models.CharField(max_length=10)
    assigned_room_type = models.CharField(max_length=10)
    booking_changes = models.IntegerField()
    deposit_type = models.CharField(max_length=50)
    agent = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    days_in_waiting_list = models.IntegerField()
    customer_type = models.CharField(max_length=50)
    adr = models.FloatField(null=True, blank=True)
    required_car_parking_spaces = models.IntegerField()
    total_of_special_requests = models.IntegerField()
    reservation_status = models.CharField(max_length=50)
    reservation_status_date = models.DateField()

    def __str__(self):
        return f"{self.hotel} booking on {self.reservation_status_date}"

class QueryHistory(models.Model):
    query_text = models.TextField()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query at {self.created_at}: {self.query_text[:50]}"
