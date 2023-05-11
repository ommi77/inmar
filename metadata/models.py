from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="departments"
    )
    name = models.CharField(max_length=100)


class Category(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=100)


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    name = models.CharField(max_length=100)


class SKU(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
