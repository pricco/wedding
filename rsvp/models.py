from django.db import models
import random


def random_code():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789') for _ in range(3))


HOST = (
    ('N', 'Natalia',),
    ('P', 'Pablo',)
)

STATUSES = (
    ('A', 'Added',),
    ('R', 'Removed',),
    ('P', 'Printed',),
    ('D', 'Invited',),
    ('C', 'Confirmed',),
)


ATTENDANCE = (
    ('U', 'Unknown',),
    ('Y', 'Yes',),
    ('N', 'No',),
)


class Group(models.Model):

    code = models.CharField(max_length=3, unique=True, default=random_code)
    invited_by = models.CharField(choices=HOST, max_length=1)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUSES)
    comment = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    called = models.BooleanField(default=False)
    web = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def count(self):
        return len(self.guests.all())

    #@property
    def guests_names(self):
        return ', '.join([guest.name for guest in self.guests.all()])
    guests_names.short_description = 'Guests'

    @property
    def attendance(self):
        return len(filter(lambda g: g.attendance == 'Y', self.guests.all()))

    def __str__(self):
        return self.name


class Guest(models.Model):

    group = models.ForeignKey(Group, related_name='guests')
    name = models.CharField(max_length=200)
    attendance = models.CharField(max_length=1, choices=ATTENDANCE, default='U')
    diabetic = models.BooleanField(default=False)
    celiac = models.BooleanField(default=False)
    child = models.BooleanField(default=False)
    table = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name