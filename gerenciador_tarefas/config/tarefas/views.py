from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
 def detalhe_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

def adicionar_tarefa(request):
    if request.method == 'post':
        titulo = request.post.get('titulo')
        descricao = request.post.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
    return redirect('lista_tarefas')
