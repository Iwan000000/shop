from django.urls import path
from django.views.decorators.cache import cache_page
from shoping.views import product_information, category, ProductListView, ReviewsCreateView, \
    your_review, ReviewsUpdateView, ReviewsDeleteView, ReviewsDetailView, ReviewsListView, AllReviewsListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'shoping'

urlpatterns = [
    path('', category, name="category_list"),
    path('<int:pk>/', ProductListView.as_view(), name="product_list"),
    path('<int:pk>/product_information/', cache_page(60)(product_information), name="product_information"),
    path('reviews/', ReviewsListView.as_view(), name="reviews"),
    path('all_reviews/', AllReviewsListView.as_view(), name="all_reviews"),
    path('<int:pk>/your_review/', your_review, name="your_review"),
    path('shoping/create/', ReviewsCreateView.as_view(), name="reviews_create"),
    path('shoping/edit/<int:pk>/', ReviewsUpdateView.as_view(), name="reviews_update"),
    path('delete/<int:pk>/', ReviewsDeleteView.as_view(), name="reviews_confirm_delete"),
    path('shoping/reviews/<int:pk>/', ReviewsDetailView.as_view(), name="reviews_detail"),
    path('create/', ProductCreateView.as_view(), name="product_create"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="product_update"),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),


]

