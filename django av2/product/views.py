from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'valor']
    success_url = reverse_lazy('product_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'valor']
    success_url = reverse_lazy('product_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('product_list')
