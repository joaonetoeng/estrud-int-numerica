from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import IntNumerica
from .form import IntNumericaForm


@login_required
def index_int_numerica(request):
    lista = IntNumerica.objects.all()
    return render(request, 'int-numerica-lista.html', {'lista': lista})

@login_required
def new_int_numerica(request):
    if request.method == 'POST':

        form = IntNumericaForm(request.POST)

        if form.is_valid():
            l = form.cleaned_data['l']
            discretizar = form.cleaned_data['discretizar']

            # Calculo aqui
            deltal = l / discretizar
            secoes = discretizar + 1
            secoes = range(1, secoes + 1)
            reserva = l
            xis=[]
            i_xi = 0
            while(reserva>0):
                reserva = l - (deltal * i_xi)
                xis.append(round(reserva,2))
                i_xi += 1
            data = [
                {'secoes': secoes},
                {'xis': xis}
            ]
            return render(request, 'new_int_numerica.html', {'form': form, 'data': data})

    else:
        form = IntNumericaForm()
    return render(request, 'new_int_numerica.html', {'form': form})
