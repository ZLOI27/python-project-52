from django import forms

from labels.models import Label


class LabelsForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ("name",)
