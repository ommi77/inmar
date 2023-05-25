from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from rest_framework_simplejwt.tokens import AccessToken

from metadata.models import Location, Department, Category, SubCategory, SKU
from metadata.serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)
from ..views import SKUViewSet


class LocationViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        # Create some test data
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = str(AccessToken().for_user(self.user))

        Location.objects.create(name="Location 1")

    def test_list_locations(self):
        url = reverse("location-list")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 200)

        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_retrieve_location(self):
        location = Location.objects.first()
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        url = reverse("location-detail", kwargs={"pk": location.id})
        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, 200)

        serializer = LocationSerializer(location)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_create_location(self):
        url = reverse("location-list")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {"name": "New Location"}
        response = self.client.post(url, **headers, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        location = Location.objects.last()
        serializer = LocationSerializer(location)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_update_location(self):
        location = Location.objects.first()
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        url = reverse("location-detail", kwargs={"pk": location.pk})
        data = {"name": "Updated Location", "city": "Updated City"}
        response = self.client.put(url, **headers, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        location.refresh_from_db()
        self.assertEqual(location.name, "Updated Location")

    def test_destroy_location(self):
        location = Location.objects.first()
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        url = reverse("location-detail", kwargs={"pk": location.pk})
        response = self.client.delete(url, **headers)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Location.objects.filter(pk=location.pk).exists())


class DepartmentViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = str(AccessToken().for_user(self.user))
        self.location1 = Location.objects.create(name="Location 1")
        self.location2 = Location.objects.create(name="Location 2")
        self.department = Department.objects.create(
            name="Department 1", location_id=self.location1.pk
        )

    def test_list_departments(self):
        url = reverse("department-list", kwargs={"location_id": self.location1.id})
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)
        departments = Department.objects.filter(location_id=self.location1.id)
        serializer = DepartmentSerializer(departments, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_department(self):
        url = reverse(
            "department-detail",
            kwargs={"location_id": self.location1.id, "pk": self.department.id},
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)
        serializer = DepartmentSerializer(self.department)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_department(self):
        url = reverse("department-list", kwargs={"location_id": self.location1.id})
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {"name": "New Department", "location": self.location1.id}
        response = self.client.post(url, **headers, data=data)
        department = Department.objects.latest("id")
        serializer = DepartmentSerializer(department)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_update_department(self):
        url = reverse(
            "department-detail",
            kwargs={"location_id": self.location1.id, "pk": self.department.id},
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {"name": "Updated Department", "location": self.location1.id}
        response = self.client.put(url, **headers, data=data)
        self.department.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.department.name, data["name"])

    def test_delete_department(self):
        url = reverse(
            "department-detail",
            kwargs={"location_id": self.location1.id, "pk": self.department.id},
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.delete(url, **headers)
        self.assertFalse(Department.objects.filter(id=self.department.id).exists())

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoryViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        # Create some test data
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = str(AccessToken().for_user(self.user))

        self.location = Location.objects.create(name="Location 1")
        self.department = Department.objects.create(
            name="Department 1", location=self.location
        )
        self.category1 = Category.objects.create(
            name="Category 1", department=self.department
        )
        self.category2 = Category.objects.create(
            name="Category 2", department=self.department
        )
        self.category3 = Category.objects.create(
            name="Category 3", department=self.department
        )

    def test_list_categories(self):
        url = reverse(
            "category-list",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 200)

        categories = Category.objects.filter(department=self.department)
        serializer = CategorySerializer(categories, many=True)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_retrieve_category(self):
        url = reverse(
            "category-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "pk": self.category1.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 200)

        serializer = CategorySerializer(self.category1)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_create_category(self):
        url = reverse(
            "category-list",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {
            "name": "New Category",
            "department": self.department.id,
        }
        response = self.client.post(url, **headers, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        category = Category.objects.get(name="New Category")
        serializer = CategorySerializer(category)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_update_category(self):
        url = reverse(
            "category-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "pk": self.category1.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {"name": "Updated Category", "department": self.department.id}
        response = self.client.put(url, **headers, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, "Updated Category")

    def test_destroy_category(self):
        url = reverse(
            "category-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "pk": self.category1.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = self.client.delete(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=self.category1.id).exists())


class SubCategoryViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        # Create test data: location, department, category, subcategory
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = str(AccessToken().for_user(self.user))

        self.location = Location.objects.create(name="Location 1")
        self.department = Department.objects.create(
            name="Department 1", location=self.location
        )
        self.category = Category.objects.create(
            name="Category 1", department=self.department
        )
        self.subcategory = SubCategory.objects.create(
            name="Subcategory 1", category=self.category
        )

    def test_list_subcategories(self):
        url = reverse(
            "subcategory-list",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "category_id": self.category.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 200)

        subcategories = SubCategory.objects.filter(
            category__department__location=self.location,
            category__department=self.department,
            category=self.category,
        )
        serializer = SubCategorySerializer(subcategories, many=True)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_retrieve_subcategory(self):
        url = reverse(
            "subcategory-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "category_id": self.category.id,
                "pk": self.subcategory.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, 200)

        serializer = SubCategorySerializer(self.subcategory)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_create_subcategory(self):
        url = reverse(
            "subcategory-list",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "category_id": self.category.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

        data = {"name": "New Subcategory", "category": self.category.id}
        response = self.client.post(url, **headers, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        subcategory = SubCategory.objects.get(name="New Subcategory")
        serializer = SubCategorySerializer(subcategory)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

    def test_update_subcategory(self):
        url = reverse(
            "subcategory-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "category_id": self.category.id,
                "pk": self.subcategory.id,
            },
        )
        data = {"name": "Updated Subcategory", "category": self.category.id}
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = self.client.put(url, **headers, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.subcategory.refresh_from_db()
        self.assertEqual(self.subcategory.name, "Updated Subcategory")

    def test_destroy_subcategory(self):
        url = reverse(
            "subcategory-detail",
            kwargs={
                "location_id": self.location.id,
                "department_id": self.department.id,
                "category_id": self.category.id,
                "pk": self.subcategory.id,
            },
        )
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = self.client.delete(url, **headers)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SubCategory.objects.filter(pk=self.subcategory.id).exists())


class SKUViewSetTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = str(AccessToken().for_user(self.user))
        self.view = SKUViewSet.as_view({"get": "list"})
        self.url = reverse("sku-detail")

        # Create some test SKUs
        SKU.objects.create(
            location="Location 1",
            department="Department 1",
            category="Category 1",
            subcategory="Subcategory 1",
        )
        SKU.objects.create(
            location="Location 2",
            department="Department 2",
            category="Category 2",
            subcategory="Subcategory 2",
        )

    def test_list_skus_with_metadata(self):
        metadata = "Location 1,Department 1,Category 1,Subcategory 1"
        request = self.factory.get(self.url, {"metadata": metadata})
        request.META["HTTP_AUTHORIZATION"] = f"Bearer {self.token}"
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        expected_data = SKU.objects.filter(
            location="Location 1",
            department="Department 1",
            category="Category 1",
            subcategory="Subcategory 1",
        )
        serializer = SKUSerializer(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_list_skus_with_invalid_metadata(self):
        metadata = "Invalid Metadata Format"
        request = self.factory.get(self.url, {"metadata": metadata})
        request.META["HTTP_AUTHORIZATION"] = f"Bearer {self.token}"
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

        expected_error = {
            "message": "Please provide the data in 'Location,department,Category, SubCategory' format"
        }
        self.assertEqual(response.data, expected_error)

    def test_list_skus_without_metadata(self):
        request = self.factory.get(self.url)
        request.META["HTTP_AUTHORIZATION"] = f"Bearer {self.token}"
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        expected_data = SKU.objects.all()
        serializer = SKUSerializer(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)
