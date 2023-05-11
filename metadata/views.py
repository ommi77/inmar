from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Location, Department, Category, SubCategory, SKU
from .serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        location_id = self.kwargs["location_id"]
        queryset = super().get_queryset()
        queryset = queryset.filter(location_id=location_id)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
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
    permission_classes = [IsAuthenticated]
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    def list(self, request, *args, **kwargs):
        metadata = request.GET.get("metadata", None)
        if metadata:
            metadata_list = [item.strip() for item in metadata.split(',')]
            if len(metadata_list) >= 4:
                queryset = self.queryset.filter(
                    location=metadata_list[0],
                    department=metadata_list[1],
                    category=metadata_list[2],
                    subcategory=metadata_list[3]
                )
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)
            else:
                message = "Please provide the data in 'Location,department,Category, SubCategory' format"
                return Response(
                    {"message": message},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return super().list(request, *args, **kwargs)
