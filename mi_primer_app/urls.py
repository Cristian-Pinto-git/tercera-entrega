from django.urls import path

from .views import (saludo, docentes, estudiantes, saludo_con_template, crear_docente, inicio,
                    crear_curso, crear_estudiante, buscar_cursos, buscar_docentes, buscar_estudiantes, cursos,
                    AutoListView, AutoCreateView, AutoDetailView, AutoUpdateView, AutoDeleteView)

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

    # urls con vistas basadas en clases
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
    path('editar/<int:pk>', AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>', AutoDeleteView.as_view(), name='eliminar-auto'),
]
