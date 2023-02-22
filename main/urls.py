from django.urls import path,include

from . import views 
app_name='main'

urlpatterns=[
    path('',views.homepage, name='homepage'),
    path('registro/',views.registro,name="registro"),
    path('logout/',views.logout_request,name="logout"),
    path('login/',views.login_request, name="login"),
    path('inventario/',views.inventario,name="inventario"),
    path('administrar/',views.gestionRepuestos,name="administrar"),
    path('registrarRepuesto/',views.registrarRepuesto),
    path('edicion/<id>', views.edicion),
    path('editar/',views.editar),
    path('eliminar/<id>', views.eliminar),
    path('enviarCorreo/',views.enviarCorreo),

]