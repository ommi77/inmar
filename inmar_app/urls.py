from django.urls import path

from .views import (
    LocationViewSet,
    DepartmentViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    SKUViewSet,
)

urlpatterns = [
    # Location
    path(
        "location/",
        LocationViewSet.as_view({"get": "list", "post": "create"}),
        name="location-list",
    ),
    path(
        "location/<int:pk>/",
        LocationViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="location-detail",
    ),
    # Department
    path(
        "location/<int:location_id>/department/",
        DepartmentViewSet.as_view({"get": "list", "post": "create"}),
        name="department-list",
    ),
    path(
        "location/<int:location_id>/department/<int:pk>/",
        DepartmentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="department-detail",
    ),
    # Category
    path(
        "location/<int:location_id>/department/<int:department_id>/category/",
        CategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="category-list",
    ),
    path(
        "location/<int:location_id>/department/<int:department_id>/category/<int:pk>/",
        CategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="category-detail",
    ),
    # SubCategory
    path(
        "location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/",
        SubCategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="subcategory-list",
    ),
    path(
        "location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/<int"
        ":pk>/",
        SubCategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="subcategory-detail",
    ),
    # Sku
    path(
        "sku/list/",
        SKUViewSet.as_view({"get": "list", "post": "create"}),
        name="sku-detail",
    ),
    path(
        "sku/<str:pk>/",
        SKUViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="sku-detail",
    ),
]
