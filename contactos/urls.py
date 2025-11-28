from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contactos", views.ContactoViewSet)

# app_name = 'contactos'

urlpatterns = [
    path("api", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('editar/<int:contacto_id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('detalle/<int:contacto_id>/', views.detalle_contacto, name='detalle_contacto'),
            # Rutas JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]