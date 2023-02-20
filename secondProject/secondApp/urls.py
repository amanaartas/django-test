from django.urls import path
from .views import(
    SecondAPI
)
urlpatterns = [
    path('second/', SecondAPI.as_view()),
]