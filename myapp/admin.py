from django.contrib import admin
from .models import Book, UserAdmin, Worker, TimeSlot, Booking, Weekday

# Register your models here.
admin.site.register(Book)
admin.site.register(UserAdmin)
admin.site.register(Worker)
admin.site.register(TimeSlot)
admin.site.register(Booking)
admin.site.register(Weekday)
