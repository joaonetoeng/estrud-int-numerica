from django import forms

from .models import IntNumerica

class IntNumericaForm(forms.ModelForm):

    class Meta:
        model = IntNumerica
        fields = ('descricao', 'l', 'discretizar', 'p', 'm', 'h', 'q', 'ei')
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'l': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'discretizar': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'p': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'm': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'h': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'q': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ei': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }