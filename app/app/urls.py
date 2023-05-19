from django.urls import path

from .views import cpu_bound, io_bound

urlpatterns = [
    path('api/cpu-bound/', cpu_bound),
    path('api/io-bound/', io_bound),
]
