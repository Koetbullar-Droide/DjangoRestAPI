from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class UserAdmin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user_admin = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Weekday(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    reccuring = models.BooleanField(default=False)
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE, blank=True, null=True)
    absence = models.BooleanField(default=False)

    def __str__(self):
        return str(self.start_time)

class Booking(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_time)
    