from django import forms
from .models import Apply

class ApplyForm(Forms.ModelForm):
    class Meta():
        model = Apply
        fields = ['applyname','phone']