from django import forms
from .models import Konsultatsiya


class KonsultatsiyaForms(forms.ModelForm):
    class Meta:
        model = Konsultatsiya
        fields = "__all__"