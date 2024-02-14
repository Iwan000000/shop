from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404

from shoping.models import Category, Product, Reviews, Version
from shoping.forms import ProductForm, VersionForm
from pytils.translit import slugify
from shoping.services import get_cached_categories



# class CategoryListView(ListView):
#     model = Category
#     extra_context = {
#         "title": "мясо свежее"
#     }

def category(request):
    context = {
        'object_list': get_cached_categories(),
        'title': 'мясо свежее'
    }
    return render(request, 'shoping/category_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get("pk"))
        context_data["object_list"] = Product.objects.filter(category_id=self.kwargs.get("pk"))
        context_data["title"] = f"{category_item.name}"

        return context_data


def product_information(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
    }

    return render(request, 'shoping/product_information.html', context)


class ReviewsListView(ListView):
    model = Reviews
    template_name = 'shoping/reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset

class AllReviewsListView(ListView):
    model = Reviews
    template_name = 'shoping/all_reviews.html'
    context_object_name = 'all_reviews'


def your_review(request, pk):
    reviews = Reviews.objects.get(pk=pk)
    context = {
        'object': reviews,
    }
    return render(request, 'shoping/../static/your_review.html', context)

class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ('title', 'content', 'preview')


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse('shoping:reviews_detail', args=[self.kwargs.get('pk')])

class ReviewsUpdateView(UpdateView):
    model = Reviews
    fields = ('title', 'content', 'preview')


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shoping:reviews_detail', args=[self.kwargs.get('pk')])

class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = reverse_lazy('shoping:reviews')

class ReviewsDetailView(DetailView):
    model = Reviews

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.number_of_views += 1
        obj.save()

        return obj



class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm
    permission_required = 'shoping.change_product'

    def get_success_url(self):
        return reverse('shoping:product_information', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
        else:
            formset = version_formset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)



    def get_object(self, queryset=None):
        product = super().get_object(queryset=queryset)
        if product.editor != self.request.user:
            raise Http404("не твой товар")
        else:
            return product



class ProductCreateView(LoginRequiredMixin, CreateView):

    model = Product
    form_class = ProductForm
    permission_required = 'shoping.change_product'
    success_url = reverse_lazy('shoping:category_list')



    def form_valid(self, form):
        self.object = form.save()
        self.object.editor = self.request.user
        self.object.save()

        return super().form_valid(form)


    def create_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                return redirect('product_detail', pk=product.pk)
        else:
            form = ProductForm()
        return render(request, 'create_product.html', {'form': form})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'shoping.delete_product'
    success_url = reverse_lazy('shoping:category_list')

    def has_permission(self):
        product = self.get_object()
        return product.has_permission_to_delete(self.request.user)
