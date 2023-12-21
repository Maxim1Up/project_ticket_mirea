from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, User, Ticket
from .forms import EventForm, UserForm, TicketForm

def reservations_page(request):
    return render(request, 'reservations/reservations_page.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'reservations/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'reservations/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'reservations/event_form.html', {'form': form, 'action': 'Create'})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'reservations/event_form.html', {'form': form, 'action': 'Update'})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'reservations/event_confirm_delete.html', {'event': event})

def user_list(request):
    users = User.objects.all()
    return render(request, 'reservations/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    tickets_user = Ticket.objects.filter(buyer_id=pk).all()
    return render(request, 'reservations/user_detail.html', {'user': user, 'tickets_user': tickets_user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'reservations/user_form.html', {'form': form, 'action': 'Create'})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'reservations/user_form.html', {'form': form, 'action': 'Update'})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'reservations/user_confirm_delete.html', {'user': user})

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'reservations/ticket_list.html', {'tickets': tickets})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'reservations/ticket_detail.html', {'ticket': ticket})

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'reservations/ticket_form.html', {'form': form, 'action': 'Create'})

def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'reservations/ticket_form.html', {'form': form, 'action': 'Update'})

def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'reservations/ticket_confirm_delete.html', {'ticket': ticket})
