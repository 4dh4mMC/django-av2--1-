from django.urls import path
from .views import ProdutoListView, ProdutoDetailView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProdutoDetailView.as_view(), name='product_detail'),
    path('product/add/', ProdutoCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProdutoUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='product_delete'),
]