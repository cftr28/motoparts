from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages 
from django.http import HttpResponse
from .models import Categoria,Repuesto
from .Carrito import Carrito
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
#from motoparts.main.models import Producto

def homepage(request):
    return render(request,'main/inicio.html',{"repuestos":Repuesto.objects.all})

def registro(request):
    
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario= form.save()
            nombre_usuario=form.cleaned_data.get('username')
            messages.success(request,f"Cuenta nueva Creada: {nombre_usuario}")
            login(request,usuario)
            messages.info(request,f"Te has logueado como: {nombre_usuario}")
            return redirect ("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    
    
    form=UserCreationForm
    return render(request,'main/registro.html',{"form":form})
def logout_request (request):
    logout(request)
    messages.info(request,"Cerrar sesion(Exitoso)")
    return redirect("main:homepage")

def login_request(request):
    
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            user=authenticate(username=usuario,password=contraseña)
            
            if user is not None:
                login(request,user)
                messages.info(request,f"Estas logueado como {usuario}")
                return redirect("main:homepage")
            else:
                messages.error(request,"Usuario o contraseña incorrecta")
        else:
            messages.error(request,"Datos erroneos")
    form=AuthenticationForm()
    return render(request,"main/login.html",{"form":form})
    
# Create your views here.
def tienda(request):
    repuestos = Repuesto.objects.all()
    return render(request,"tienda.html", {'repuestos':repuestos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(id=producto_id)
    carrito.agregar(repuesto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(id=producto_id)
    carrito.eliminar(repuesto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(id=producto_id)
    carrito.restar(repuesto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def inventario(request):
    repuestos = Repuesto.objects.all()
    return render(request,"inventario.html", {'repuestos':repuestos})


def gestionRepuestos(request):
    repuestos=Repuesto.objects.all()
    return render(request,"gestionRepuestos.html",{"repuestos":repuestos})

def registrarRepuesto(request):
    nombre=request.POST['txtnombre']
    categoria=request.POST['txtcategoria']
    descripcion=request.POST['txtdescripcion']
    precio=request.POST['txtprecio']
    cantidad=request.POST['txtcantidad']
    imagen=request.FILES.get('txtimagen1')
    ProductoNuevo =  Repuesto.objects.create(nombre=nombre,categoria=categoria,descripcion=descripcion,precio=precio,cantidad=cantidad,imagen=imagen)
    messages.success(request,'Repuesto añadido')
    return redirect('/administrar')

def edicion(request, id):
    repuestos = Repuesto.objects.get(id=id)
    return render(request, "edicionRepuesto.html", {"repuestos": repuestos})

def editar(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    categoria=request.POST['txtcategoria']
    descripcion=request.POST['txtdescripcion']
    precio=request.POST['txtprecio']
    cantidad=request.POST['txtcantidad']
    imagen=request.FILES.get('txtimagen2')
    repuestos=Repuesto.objects.get(id=id)
    repuestos.nombre=nombre
    repuestos.categoria=categoria
    repuestos.descripcion=descripcion
    repuestos.precio=precio
    repuestos.cantidad=cantidad
    repuestos.imagen=imagen
    repuestos.save()
    messages.success(request,'Edicion exitosa')
    return redirect('/administrar')


def eliminar(request,id):
    repuesto=Repuesto.objects.get(id=id)
    repuesto.delete()
    messages.success(request,'Usted elimino con exito el repuesto')
    return redirect('/administrar')


def send_email(mail):
    context = {'mail':mail}
    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo Compra',
        'MotoParts',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

# Create your views here.
def enviarCorreo(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)
        print('Correo enviado')
    return redirect('Tienda')