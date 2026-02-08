from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__' # DEFINE QUE VAI USAR TODOS OS FIELDS DO FORM
