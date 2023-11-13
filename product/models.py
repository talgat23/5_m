from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


STARS = (
    (1, '* '),
    (2, '* ' * 2),
    (3, '* ' * 3),
    (4, '* ' * 4),
    (5, '* ' * 5),
)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5)

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

