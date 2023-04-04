from django.shortcuts import render
from .models import Pais, Localizacion, Puesto, Salario, Fabrica, Empleado
from django.http import HttpResponse

def create(request):
    # Paises
    # p1 = Pais(pais='Andorra', codigo=376)
    # p1.save()
    # p2 = Pais(pais='Bulgaria', codigo=359)
    # p2.save()
    # p3 = Pais(pais='Canadá', codigo=1)
    # p3.save()
    # p4 = Pais(pais='Dinamarca', codigo=45)
    # p4.save()
    # p5 = Pais(pais='Hong Kong', codigo=852)
    # p5.save()
    # p6 = Pais(pais='Ucrania', codigo=380)
    # p6.save()

    # # Localizaciónes
    # l1 = Localizacion(nombre='Burnaby', pais=p3)
    # l1.save()
    # l2 = Localizacion(nombre='Dunham', pais=p3)
    # l2.save()
    # l3 = Localizacion(nombre='Les Bons', pais=p1)
    # l3.save()
    # l4 = Localizacion(nombre='Sofia',pais=p2)
    # l4.save()
    # l5 = Localizacion(nombre='Pleven',pais=p2)
    # l5.save()
    # l6 = Localizacion(nombre='Odense',pais=p4)
    # l6.save()
    # l7 = Localizacion(nombre='Taastrup',pais=p4)
    # l7.save()
    # l8 = Localizacion(nombre='Kowloon',pais=p5)
    # l8.save()
    # l9 = Localizacion(nombre='Kiev',pais=p6)
    # l9.save()
    # l10 = Localizacion(nombre='Lugansk',pais=p6)
    # l10.save()
    
    # # Salarios
    # s1 = Salario(bruto=230000, extra_diciembre=False, extra_junio=True)
    # s1.save()
    # s2 = Salario(bruto=320000, extra_diciembre=False, extra_junio=False)
    # s2.save()
    # s3 = Salario(bruto=500000, extra_diciembre=True, extra_junio=True)
    # s3.save()
    # s4 = Salario(bruto=280000, extra_diciembre=True, extra_junio=False)
    # s4.save()

    # # Puestos
    # pu1 = Puesto(nombre='Diseñador', descripcion='', salario=s1)
    # pu1.save()
    # pu2 = Puesto(nombre='Administración', descripcion='', salario=s4)
    # pu2.save()
    # pu3 = Puesto(nombre='Gerente', descripcion='', salario=s3)
    # pu3.save()
    # pu4 = Puesto(nombre='Desarrollador Web', descripcion='', salario=s2)
    # pu4.save()

    # # Fabricas 
    # f1 = Fabrica(nombre='Nike 1', direccion='Les bons 123', codigo_postal='456', localizacion=l3)
    # f1.save()
    # f2 = Fabrica(nombre='Nike 2', direccion='Kiev 789', codigo_postal='1012', localizacion=l9)
    # f2.save()
    # f3 = Fabrica(nombre='Nike 3', direccion='Odense 375', codigo_postal='8888', localizacion=l6)
    # f3.save()

    # #Empleados
    # e1 = Empleado(nombre='Pepito',apellido='Suarez', dni='00000000', email='elpepis@gmail.com', direccion='Calle Almendros, número 15', puesto=pu2,fabrica=f1)
    # e1.save()
    # e2 = Empleado(nombre='Julia',apellido='Hernández', dni='00000001',email='juliahernandez_96@gmail.com',  direccion='Avenida Libertad, número 23', puesto=pu1,fabrica=f3)
    # e2.save()
    # e3 = Empleado(nombre='Carlos',apellido='Rodriguez', dni='42312695', email='carlos.rodriguez_83@hotmail.com', direccion='Calle del Sol, número 10', puesto=pu2,fabrica=f2)
    # e3.save()
    # e4 = Empleado(nombre='María',apellido='Gonzalez', dni='32195764',email='mariagonzalez_2001@yahoo.com',  direccion='Paseo de la Montaña, número 7,', puesto=pu3,fabrica=f3)
    # e4.save()
    # e5 = Empleado(nombre='Juan',apellido='Ramirez', dni='40259551',email='juan.ramirez_77@outlook.com',  direccion='Calle de la Paz, número 18', puesto=pu1,fabrica=f1)
    # e5.save()
    # e6 = Empleado(nombre='Ana',apellido='López', dni='20134569',email='analopez_94@gmail.com',  direccion='Carrera del Río, número 4', puesto=pu4,fabrica=f1)
    # e6.save()
    # e7 = Empleado(nombre='Miguel',apellido='Torres', dni='16452305',email='migueltorres_85@yahoo.es',  direccion='Avenida de los Olivos, número 12', puesto=pu2,fabrica=f3)
    # e7.save()
    # e8 = Empleado(nombre='Laura',apellido='Sánchez', dni='30001465',email='laura.sanchez_92@icloud.com',  direccion='Calle del Mar, número 9', puesto=pu4,fabrica=f2)
    # e8.save()
    # e9 = Empleado(nombre='Luis',apellido='García', dni='37521694',email='luisgarcia_88@gmail.com',  direccion='Plaza del Oeste, número 6', puesto=pu4,fabrica=f3)
    # e9.save()
    # e10 = Empleado(nombre='Lucia',apellido='Perez', dni='22653154',email='lucia.perez_90@hotmail.es',  direccion='Diagonal Palermo, número 76', puesto=pu3,fabrica=f3)
    # e10.save()
    
    return HttpResponse('Creado')

def inicio(request):
    return render(request, 'inicio.html', {})

def sucursales(request):
    fabricas = Fabrica.objects.all()
    return render(request, 'sucursales.html', {'fabricas':fabricas})

def nosotros(request):
    contexto = {
        'paises': Pais.objects.all().count(),
        'empleados': Empleado.objects.all().count(),
        'lista_paises':Pais.objects.all()
    }
    return render(request, 'nosotros.html', contexto)

def sucursal(request, id):
    sucursal = Fabrica.objects.get(id=id)
    contexto = {
        'id':id,
        'sucursal': sucursal,
        'empleados': sucursal.empleado_set.all()
    }
    return render(request, 'sucursal.html', contexto)

def empleados(request):
    empleados_por_puesto = []

    for puesto in Puesto.objects.all():
        empleados = Empleado.objects.filter(puesto=puesto)
     
        empleados_por_puesto.append((puesto, empleados))
        
    return render(request, 'empleados.html', {'lista': empleados_por_puesto})

def empleado(request, dni):
    empleado = Empleado.objects.get(dni= dni)
   
    return render(request, 'empleado.html', {'empleado':empleado})

def pais(request, id):
    pais = Pais.objects.get(id=id)
    ciudades = pais.localizacion_set.all()
    context = {
        'pais': pais,
        'ciudades': ciudades,
    }
    return render(request, 'pais.html', context)