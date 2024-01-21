from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from shoping.models import Category, Product, Reviews

from pytils.translit import slugify


class CategoryListView(ListView):
    model = Category
    extra_context = {
        "title": "мясо свежее"
    }


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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.number_of_views += 1
        self.object.save()
        return super().get(request, *args, **kwargs)
