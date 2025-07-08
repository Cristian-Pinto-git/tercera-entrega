from django.urls import path

from .views import saludo, docentes, estudiantes, saludo_con_template, crear_docente, inicio, crear_curso, crear_estudiante, buscar_cursos, buscar_docentes, buscar_estudiantes, cursos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-docente/', crear_docente, name='crear-docente'),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('docentes/', docentes, name='docentes'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
    path('estudiantes/buscar', buscar_estudiantes, name='buscar-estudiantes'),
    path('docentes/buscar', buscar_docentes, name='buscar-docentes'),
]
