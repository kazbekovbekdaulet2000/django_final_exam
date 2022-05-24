from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Rental API",
        default_version='v1',
        description="desc",
        contact=openapi.Contact(email="kazbekov.bekdaulet2000@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('core/', include('book_journal.urls')),
    # Swagger
    path('docs/swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('docs/swagger/api.json/',schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('docs/swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
