from django.urls import path
from sliders.views import experiments_view

urlpatterns = [
    path('other/', experiments_view, name='other'),
]