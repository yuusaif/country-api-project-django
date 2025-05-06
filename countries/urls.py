from django.urls import path
from .views import FetchCountriesView

urlpatterns = [
    path('fetch/', FetchCountriesView.as_view(), name='fetch'),
]
