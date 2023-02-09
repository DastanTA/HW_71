from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from ebay.models import Product
from ebay.views.base_views import SearchView
from ebay.forms import ProductForm, SimpleSearchForm

Product.objects.all().order_by("category", "name").filter(remainder__gt=0)


class AllProductsView(SearchView):
    model = Product
    ordering = ['category', 'name']
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1
    search_form_class = SimpleSearchForm
    search_fields = ['name__icontains', 'description__icontains']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(remainder__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'products/create_product.html'
    form_class = ProductForm
    permission_required = 'ebay.add_product'
    permission_denied_message = "You don't have rights for this action!"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = 'ebay.add_product'
    permission_denied_message = "You don't have rights for this action!"

    def get_success_url(self):
        return reverse('ebay:view_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('ebay:all_products')
    permission_required = 'ebay.add_product'
    permission_denied_message = "You don't have rights for this action!"
