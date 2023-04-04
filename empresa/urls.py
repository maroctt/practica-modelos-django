from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path("inicio/", views.inicio, name='inicio'),
    path("sucursales/", views.sucursales, name='sucursales'),
    path("sucursales/<int:id>", views.sucursal, name='sucursal'),
    path("nosotros/", views.nosotros, name='nosotros'),
    path("empleados/", views.empleados, name='empleados'),
    path('empleados/<str:dni>', views.empleado, name='empleado'),
    path('pais/<int:id>', views.pais, name='pais'),
]
