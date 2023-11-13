from django.urls import path

from .views import (
    ProductListAPIView,
    ProductDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, ReviewListAPIView, ReviewDetailAPIView,
    ProductReviewListAPIView,
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('review/', ReviewListAPIView.as_view()),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('product_review/', ProductReviewListAPIView.as_view()),
]

# urlpatterns = [
#     path('category/', views.category_list_api_view),
#     path('category/<int:id>/', views.category_detail_api_view),
#     path('product/', views.product_list_api_view),
#     path('product/<int:id>/', views.product_detail_api_view),
#     path('reviews/', views.review_list_api_view),
#     path('reviews/<int:id>/', views.review_detail_api_view),
#     path('product_reviews/', views.product_review_list_api_view),
# ]
