from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from product.models import Category, Product, Review
from product.serializers import CategorySerializers, ProductSerializers, ReviewSerializers, \
    ProductReviewSerializers
from rest_framework import status


# @api_view(['GET', 'POST'])
# def category_list_api_view(request):
#     # if request.method == 'GET':
#     #     category = Category.objects.prefetch_related().all()
#     #     category_json = CategorySerializers(instance=category, many=True).data
#     #     return Response(data=category_json)
#     # elif request.method == 'POST':
#     #     serializer = CategorySerializers(data=request.data)
#     #     if not serializer.is_valid():
#     #         return Response(status=status.HTTP_400_BAD_REQUEST,
#     #                         data={'message': 'Request failed',
#     #                               'errors': serializer.errors})
#     #     category = Category.objects.create(name=category.name)
#     #     return Response(
#     #         data={'id': review.id, 'product': review.product.id, 'text': review.text, 'stars': review.stars},
#     #         status=status.HTTP_201_CREATED)
#     if request.method == 'GET':
#         category = Category.objects.all()
#         category_json = CategorySerializers(category, many=True).data
#         return Response(data=category_json)
#     elif request.method == 'POST':
#         serializer = CategorySerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail_api_view(request, id):
#     # try:
#     #     category = Category.objects.get(id=id)
#     # except Category.DoesNotExist:
#     #     return Response(data={'message': 'Category not found!'},
#     #                     status=status.HTTP_404_NOT_FOUND)
#     # if request.method == 'GET':
#     #     category_json = CategorySerializers(category, many=False).data
#     #     return Response(data=category_json)
#     # elif request.method == 'PUT':
#     #     category.name = request.data.get('name')
#     #     category.save()
#     #     return Response(status=status.HTTP_201_CREATED,
#     #                     data={'message': 'Category created'})
#     # elif request.method == 'DELETE':
#     #     category.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT,
#     #                     data={'message': 'Category destroyed'})
#     try:
#         queryset = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(data={'message': 'Category not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = CategorySerializers(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = CategorySerializers(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def product_list_api_view(request):
#     # if request.method == 'GET':
#     #     product = Product.objects.all()
#     #     product_json = ProductSerializers(instance=product, many=True).data
#     #     return Response(data=product_json)
#     # elif request.method == 'POST':
#     #     serializer = ProductCreateValidateSerializer(data=request.data)
#     #     if not serializer.is_valid():
#     #         return Response(status=status.HTTP_400_BAD_REQUEST,
#     #                         data={'message': 'Request failed',
#     #                               'errors': serializer.errors})
#     #     title = request.data.get('title')
#     #     description = request.data.get('description')
#     #     price = request.data.get('price')
#     #     category = request.data.get('category')
#     #
#     #     try:
#     #         category = Category.objects.get(id=category)
#     #     except Category.DoesNotExist:
#     #         return Response(data={'message': 'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
#     #     product = Product.objects.create(title=title, description=description, price=price, category=category)
#     #     return Response(data={'id': product.id, 'title': product.title, 'category': product.category.id},
#     #                     status=status.HTTP_201_CREATED)
#     if request.method == 'GET':
#         product = Product.objects.all()
#         product_json = ProductSerializers(product, many=True).data
#         return Response(data=product_json, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     # try:
#     #     product = Product.objects.get(id=id)
#     # except Product.DoesNotExist:
#     #     return Response(data={'message': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
#     #
#     # if request.method == 'GET':
#     #     product_json = ProductSerializers(product, many=False).data
#     #     return Response(data=product_json, status=status.HTTP_200_OK)
#     # elif request.method == 'PUT':
#     #     product.title = request.data.get('title')
#     #     product.save()
#     #     return Response(data={'message': 'Product updated'}, status=status.HTTP_200_OK)
#     # elif request.method == 'DELETE':
#     #     product.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#
#     try:
#         queryset = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(data={'message': 'Product not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ProductSerializers(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = ProductSerializers(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     # if request.method == 'GET':
#     #     review = Review.objects.all()
#     #     review_json = ReviewSerializers(review, many=True).data
#     #     return Response(data=review_json)
#     # elif request.method == 'POST':
#     #     product = request.data.get('product')
#     #     text = request.data.get('text')
#     #     stars = request.data.get('stars')
#     #
#     #     try:
#     #         product = Review.objects.get(id=product)
#     #     except Product.DoesNotExist:
#     #         return Response(data={'message': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
#     #     review = Review.objects.create(product=product, text=text, stars=stars)
#     #     return Response(
#     #         data={'id': review.id, 'product': review.product.id, 'text': review.text, 'stars': review.stars},
#     #         status=status.HTTP_201_CREATED)
#     if request.method == 'GET':
#         review = Review.objects.all()
#         review_json = ReviewSerializers(review, many=True).data
#         return Response(data=review_json, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     # try:
#     #     review = Review.objects.get(id=id)
#     # except Review.DoesNotExist:
#     #     return Response(data={'message': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
#     #
#     # if request.method == 'GET':
#     #     review_json = ReviewSerializers(review, many=False).data
#     #     return Response(data=review_json, status=status.HTTP_200_OK)
#     # elif request.method == 'PUT':
#     #     review.title = request.data.get('title')
#     #     review.save()
#     #     return Response(data={'message': 'Review updated'}, status=status.HTTP_200_OK)
#     # elif request.method == 'DELETE':
#     #     review.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     try:
#         queryset = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'message': 'Review not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewSerializers(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializers(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def product_review_list_api_view(request):
#     product = Product.objects.all()
#     product_json = ProductReviewSerializers(product, many=True).data
#     return Response(data=product_json)


class ProductReviewListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializers


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
