from django.db import models

# Create your models here.

class AutosNuevos(models.Model):
    marca = models.models.CharField(max_lenght=30)
    modelo = models.models.CharField(max_lenght=30)
    version = models.models.CharField(max_lenght=30)
    fecha_de_fabricacion = models.DateField(null=True)
    color = models.models.CharField(max_lenght=30)
    

class AutosUsados(models.Model):
    marca = models.models.CharField(max_lenght=30)
    modelo = models.models.CharField(max_lenght=30)
    version = models.models.CharField(max_lenght=30)
    color = models.models.CharField(max_lenght=30)
    fecha_de_fabricacion = models.DateField(null=True)
    fecha_de_patentacion = models.DateField(null=True)
    
    
class MotosNuevas(models.Model):
    marca = models.models.CharField(max_lenght=30)
    modelo = models.models.CharField(max_lenght=30)
    cilindrada = models.models.CharField(max_lenght=30)
    color = models.models.CharField(max_lenght=30)
    fecha_de_fabricacion = models.DateField(null=True)
        
    
class MotosUsadas(models.Model):
    marca = models.models.CharField(max_lenght=30)
    modelo = models.models.CharField(max_lenght=30)
    cilindrada = models.models.CharField(max_lenght=30)
    color = models.models.CharField(max_lenght=30)
    fecha_de_fabricacion = models.DateField(null=True)
    fecha_de_patentacion = models.DateField(null=True)    
    
    

    


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"({self.camada}) {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
