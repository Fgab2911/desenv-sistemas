from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
 def detalhe_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})