from django.contrib import admin
from django.urls import path, include
from inmar_app.urls import urlpatterns as inmar_app_uls
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(inmar_app_uls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
