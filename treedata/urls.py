from django.urls import path
from .views import app_one_view,app_two_view

urlpatterns = [
    path('accountone/', app_one_view),
    path('accounttwo/',app_two_view)
]