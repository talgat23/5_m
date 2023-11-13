from rest_framework import serializers
from product.models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.products.count()
        # depth = 1


class ProductSerializers(serializers.ModelSerializer):
    tag = TagSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def validate_category_id(self, value):
        for tag_id in value:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                raise ValidationError('Tag does not exixt!')
        return value


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0
