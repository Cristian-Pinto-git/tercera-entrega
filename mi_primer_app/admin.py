from django.contrib import admin

# Register your models here.
from .models import Docente, Curso, Estudiante

register_models = [Docente, Curso, Estudiante]

admin.site.register(register_models)
