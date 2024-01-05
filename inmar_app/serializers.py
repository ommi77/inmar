from rest_framework import serializers

from .models import Location, Department, Category, SubCategory, SKU


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        db_table =Location
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = Department
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        db_table = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        db_table = SubCategory
        fields = "__all__"
