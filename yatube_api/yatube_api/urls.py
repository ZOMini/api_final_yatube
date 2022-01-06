# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="API",
#         default_version='v1',
#         description="Документация для приложения API проекта
#                       API_FINAL_YATUBE",
#         # terms_of_service="URL страницы с пользовательским соглашением",
#         contact=openapi.Contact(email="admin@kittygram.ru"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
# urlpatterns += [
#     url(r'^swagger(?P<format>\.json|\.yaml)$',
#         schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
#         name='schema-swagger-ui'),
#     url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
#         name='schema-redoc'),
# ]
