from django.db import models

class Pais(models.Model):
    pais = models.CharField(max_length=50)
    codigo = models.IntegerField()

    def __str__(self):
        return self.pais

class Localizacion(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Salario(models.Model):
    bruto = models.DecimalField(decimal_places=2, max_digits=8)
    extra_diciembre = models.BooleanField()
    extra_junio = models.BooleanField()

    def __str__(self):
        return self.bruto

class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=10)  
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(null=True)
    direccion = models.CharField(max_length=250, null=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre




