from django import forms

from .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('신청금액', '신청기간',)