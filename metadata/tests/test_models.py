from django.test import TestCase
from metadata.models import Location, Department, Category, SubCategory, SKU

class LocationModelTestCase(TestCase):
    def test_location_creation(self):
        location = Location.objects.create(name="Location 1")
        self.assertEqual(location.name, "Location 1")

class DepartmentModelTestCase(TestCase):
    def test_department_creation(self):
        location = Location.objects.create(name="Location 1")
        department = Department.objects.create(location=location, name="Department 1")
        self.assertEqual(department.location, location)
        self.assertEqual(department.name, "Department 1")

class CategoryModelTestCase(TestCase):
    def test_category_creation(self):
        location = Location.objects.create(name="Location 1")
        department = Department.objects.create(location=location, name="Department 1")
        category = Category.objects.create(department=department, name="Category 1")
        self.assertEqual(category.department, department)
        self.assertEqual(category.name, "Category 1")

class SubCategoryModelTestCase(TestCase):
    def test_subcategory_creation(self):
        location = Location.objects.create(name="Location 1")
        department = Department.objects.create(location=location, name="Department 1")
        category = Category.objects.create(department=department, name="Category 1")
        subcategory = SubCategory.objects.create(category=category, name="Subcategory 1")
        self.assertEqual(subcategory.category, category)
        self.assertEqual(subcategory.name, "Subcategory 1")

class SKUModelTestCase(TestCase):
    def test_sku_creation(self):
        sku = SKU.objects.create(
            sku="SKU1",
            name="Product 1",
            location="Location 1",
            department="Department 1",
            category="Category 1",
            subcategory="Subcategory 1"
        )
        self.assertEqual(sku.sku, "SKU1")
        self.assertEqual(sku.name, "Product 1")
        self.assertEqual(sku.location, "Location 1")
        self.assertEqual(sku.department, "Department 1")
        self.assertEqual(sku.category, "Category 1")
        self.assertEqual(sku.subcategory, "Subcategory 1")
