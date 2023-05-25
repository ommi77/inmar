from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Location, Department, Category, SubCategory, SKU
from .serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing locations.

    Requires authentication for all operations.

    Supported actions:
    - list: Get a list of all locations
    - retrieve: Get details of a specific location
    - create: Create a new location
    - update: Update an existing location
    - partial_update: Partially update an existing location
    - destroy: Delete an existing location
    """

    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing departments.

    Requires authentication for all operations.

    Supported actions:
    - list: Get a list of all departments
    - retrieve: Get details of a specific department
    - create: Create a new department
    - update: Update an existing department
    - partial_update: Partially update an existing department
    - destroy: Delete an existing department
    """

    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        location_id = self.kwargs["location_id"]
        queryset = super().get_queryset()
        queryset = queryset.filter(location_id=location_id)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing categories.

    Requires authentication for all operations.

    Supported actions:
    - list: Get a list of all categories
    - retrieve: Get details of a specific category
    - create: Create a new category
    - update: Update an existing category
    - partial_update: Partially update an existing category
    - destroy: Delete an existing category
    """

    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        location_id = self.kwargs["location_id"]
        department_id = self.kwargs["department_id"]
        queryset = super().get_queryset()
        queryset = queryset.filter(
            department_id=department_id, department__location_id=location_id
        )
        return queryset


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing subcategories.

    Requires authentication for all operations.

    Supported actions:
    - list: Get a list of all subategories
    - retrieve: Get details of a specific subcategory
    - create: Create a new subcategory
    - update: Update an existing subcategory
    - partial_update: Partially update an existing subcategory
    - destroy: Delete an existing subcategory
    """

    permission_classes = [IsAuthenticated]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        location_id = self.kwargs["location_id"]
        department_id = self.kwargs["department_id"]
        category_id = self.kwargs["category_id"]
        queryset = super().get_queryset()
        queryset = queryset.filter(
            category_id=category_id,
            category__department_id=department_id,
            category__department__location_id=location_id,
        )
        return queryset


class SKUViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing SKUs.

    Requires authentication for all operations.

    Supported actions:
    - list: Get a list of SKUs based on metadata filters
    - retrieve: Get details of a specific SKU
    - create: Create a new SKU
    - update: Update an existing SKU
    - partial_update: Partially update an existing SKU
    - destroy: Delete an existing SKU

    When using the 'list' action, provide the 'metadata' query parameter with a comma-separated string
    in the format 'Location,department,Category,SubCategory' to filter the SKUs.

    Example: /api/skus/?metadata=Center,Grocery,Crackers,Rice Cakes

    If the 'metadata' is missing or doesn't meet the required format, a 400 Bad Request response will be returned.
    """

    permission_classes = [IsAuthenticated]
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    def list(self, request, *args, **kwargs):
        metadata = request.GET.get("metadata", None)
        if metadata:
            metadata_list = [item.strip() for item in metadata.split(",")]
            if len(metadata_list) >= 4:
                queryset = self.queryset.filter(
                    location=metadata_list[0],
                    department=metadata_list[1],
                    category=metadata_list[2],
                    subcategory=metadata_list[3],
                )
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)
            else:
                message = "Please provide the data in 'Location,department,Category, SubCategory' format"
                return Response(
                    {"message": message}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return super().list(request, *args, **kwargs)
