from django import forms
from .models import Appointment
from datetime import date


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'date', 'message']

        # ✅ MUST be inside Meta
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": date.today().isoformat()
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            attrs = {'class': 'form-control'}

            # remove placeholder for date picker
            if name != "date":
                attrs['placeholder'] = field.label

            field.widget.attrs.update(attrs)