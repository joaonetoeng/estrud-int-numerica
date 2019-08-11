from django.forms import ModelForm
from .models import ProcessoPdelta

class PdeltaForm(ModelForm):
    class Meta:
        model = ProcessoPdelta
        fields = ['descricao', 'l', 'p', 'm', 'h', 'q', 'ei']