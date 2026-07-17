from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Articulo
from . import services


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'products/categoria_list.html'
    context_object_name = 'categorias'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'products/categoria_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('products:categoria_list')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'products/categoria_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('products:categoria_list')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'products/categoria_confirm_delete.html'
    success_url = reverse_lazy('products:categoria_list')


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'products/articulo_list.html'
    context_object_name = 'articulos'


class ArticuloCreateView(CreateView):
    model = Articulo
    template_name = 'products/articulo_form.html'
    fields = ['nombre', 'categoria', 'precio_venta', 'precio_compra', 'stock']
    success_url = reverse_lazy('products:articulo_list')


class ArticuloUpdateView(UpdateView):
    model = Articulo
    template_name = 'products/articulo_form.html'
    fields = ['nombre', 'categoria', 'precio_venta', 'precio_compra', 'stock']
    success_url = reverse_lazy('products:articulo_list')


class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'products/articulo_confirm_delete.html'
    success_url = reverse_lazy('products:articulo_list')
