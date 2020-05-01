from django.urls import path

from .views import schedule_view

urlpatterns = [
    path('schedule-task', schedule_view),
]
