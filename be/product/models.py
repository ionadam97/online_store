import uuid
from django.db import models
from django.core.validators import MinValueValidator


def product_image_path(instance):
    return f"uploads/products/{instance.category}/{instance.title}"


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/products", null=True, blank=True)
    thumbnail = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    delivery = models.BooleanField(default=True, null=True, blank=True)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)], blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created", "title")

    def __str__(self):
        return self.title
