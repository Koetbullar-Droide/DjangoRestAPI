from rest_framework import serializers
from .models import Book, UserAdmin, Worker, TimeSlot, Booking

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'