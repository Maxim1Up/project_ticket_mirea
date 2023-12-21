from django.urls import path
from .views import ( reservations_page,
    event_list, event_detail, event_create, event_update, event_delete,
    user_list, user_detail, user_create, user_update, user_delete,
    ticket_list, ticket_detail, ticket_create, ticket_update, ticket_delete,
)

urlpatterns = [
    path('', reservations_page, name='reservations_page'),

    
    path('events/', event_list, name='event_list'),
    path('events/create/', event_create, name='event_create'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:pk>/update/', event_update, name='event_update'),
    path('events/<int:pk>/delete/', event_delete, name='event_delete'),

    
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('users/<int:pk>/update/', user_update, name='user_update'),
    path('users/<int:pk>/delete/', user_delete, name='user_delete'),

    
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/create/', ticket_create, name='ticket_create'),
    path('tickets/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('tickets/<int:pk>/update/', ticket_update, name='ticket_update'),
    path('tickets/<int:pk>/delete/', ticket_delete, name='ticket_delete'),
]
