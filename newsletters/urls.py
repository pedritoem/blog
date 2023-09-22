from django.urls import path
from .views import newsletter_signUp, newsletter_unsubscribe

app_name="newsletters"

urlpatterns = [
    path('entrenamiento/', newsletter_signUp, name="optin"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe")
]
