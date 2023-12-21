from django import forms
from .models import Event, User, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'ticket_quantity', 'date_and_time', 'description']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = 'Название'
        self.fields['ticket_quantity'].label = 'Количество билетов'
        self.fields['date_and_time'].label = 'Дата и время'
        self.fields['description'].label = 'Описание'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'cost', 'buyer', 'is_purchased']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['event'].label = 'Мероприятие'
        self.fields['buyer'].label = 'Покупатель'
        self.fields['cost'].label = 'Стоимость'
        self.fields['is_purchased'].label = 'Статус покупки'

        
    
    
