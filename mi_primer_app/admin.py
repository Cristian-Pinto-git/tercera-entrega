from django.contrib import admin

# Register your models here.
from .models import Docente, Curso, Estudiante, Auto, User

register_models = [Docente, Curso, Estudiante, Auto, User]

admin.site.register(register_models)
