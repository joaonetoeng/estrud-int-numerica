from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import IntAnalitica


@login_required
def index_int_analitica(request):
    lista = IntAnalitica.objects.all()
    return render(request, 'int-analitica-lista.html', {'lista': lista})