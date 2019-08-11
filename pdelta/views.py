from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProcessoPdelta
from .form import PdeltaForm

@login_required
def index(request):
    lista = ProcessoPdelta.objects.all()
    return render(request, 'index.html', {'lista': lista})

@login_required
def memory_new(request):
    form = PdeltaForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('index')
    return render(request, 'pdelta_form.html', {'form': form})

@login_required
def memory_update(request, id):
    memory = get_object_or_404(ProcessoPdelta, pk=id)
    form = PdeltaForm(request.POST or None, instance=memory)

    if form.is_valid():
        form.save()

        return redirect('index')
    return render(request, 'pdelta_form.html', {'form': form})

@login_required
def memory_delete(request, id):
    memory = get_object_or_404(ProcessoPdelta, pk=id)

    if request.method == 'POST':
        memory.delete()
        return redirect('index')

    return render(request, 'memory_delete_confirm.html', {'memory': memory})