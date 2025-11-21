from django.shortcuts import render
from forms import User

# Create your views here.
def CadastraUser(request):
    if request.method == 'POST':
        form = VendaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venda Cadastrado com sucesso')
            form = VendaForms()
        else:
            messages.error(request, 'Erro ao salvar o formulário')
    else:
        form = VendaForms()
    context = { 'form':form}
    return render(request, 'cadastrovenda.html', context)