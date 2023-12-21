from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    ticket_quantity = models.IntegerField(null=True, blank=True)
    date_and_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_sold_tickets_count(self):
        return self.ticket_set.filter(is_purchased=True).count()

class User(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255,null=True, blank=True)
    purchased_tickets = models.ManyToManyField('Ticket', related_name='buyers', blank=True)

    def __str__(self):
        return self.last_name
    

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_purchased = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return self.event
    
