from django.urls import path

from .views import base_views, goal_views, level_views, channel_views, email_views, phone_views, subscribed_views

app_name = 'grandmaai'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
  
    # goal
    path('goal/create/', goal_views.goal_create, name='goal_create'),
    path('goal/modify/<int:goal_id>/', goal_views.goal_modify, name='goal_modify'),

    # level
    path('level/create/', level_views.level_create, name='level_create'),
    path('level/modify/<int:level_id>/', level_views.level_modify, name='level_modify'),

    # channel
    path('channel/create/', channel_views.channel_create, name='channel_create'),
    path('channel/modify/<int:channel_id>/', channel_views.channel_modify, name='channel_modify'),

    # email
    path('email/create/', email_views.email_create, name='email_create'),
    path('email/modify/<int:email_id>/', email_views.email_modify, name='email_modify'),

    # phone
    path('phone/create/', phone_views.phone_create, name='phone_create'),
    path('phone/modify/<int:phone_id>/', phone_views.phone_modify, name='phone_modify'),

    # Subscribed
    path('subscribed/', subscribed_views.subscribed, name='subscribed'),
    
]