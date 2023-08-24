from django.urls import path

from .views import start_order, error

urlpatterns = [
    path('start_order/', start_order, name="start_order"),
    path('error/', error, name="error")
]