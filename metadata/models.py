from django.db import models


class Location(models.Model):
    """
    Represents a location.
    """

    name = models.CharField(max_length=100)


class Department(models.Model):
    """
    Represents a department within a location.
    """

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="departments"
    )
    name = models.CharField(max_length=100)


class Category(models.Model):
    """
    Represents a category within a department.
    """

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=100)


class SubCategory(models.Model):
    """
    Represents a subcategory within a category.
    """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    name = models.CharField(max_length=100)


class SKU(models.Model):
    """
    Represents a SKU (Stock Keeping Unit).
    """

    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
