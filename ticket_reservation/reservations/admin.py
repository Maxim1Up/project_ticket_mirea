from django.contrib import admin
from reservations.models import Ticket, Event, User

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Event)
admin.site.register(User)