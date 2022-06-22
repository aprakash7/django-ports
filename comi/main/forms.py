from .models import commands
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = commands
        fields = "__all__"
