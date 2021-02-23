from django.db import models

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (type(self), self.email)


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    attended = models.BinaryField(null=True)
