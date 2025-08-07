from django.urls import path

from .views import (about, saludo, docentes, estudiantes, saludo_con_template, crear_docente, inicio,
                    crear_curso, crear_estudiante, buscar_cursos, buscar_docentes, buscar_estudiantes, cursos,
                    listar_docentes, crear_docente, detalle_docente, editar_docente, eliminar_docente, detalle_estudiante,
                    editar_estudiante, eliminar_estudiante,
                    AutoListView, AutoCreateView, AutoDetailView, AutoUpdateView, AutoDeleteView, CursoDetailView, CursoUpdateView, CursoDeleteView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-docente/', crear_docente, name='crear-docente'),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('estudiantes/<int:id>/', detalle_estudiante, name='detalle-estudiante'),
    path('estudiantes/<int:id>/editar/', editar_estudiante, name='editar-estudiante'),
    path('estudiantes/<int:id>/eliminar/', eliminar_estudiante, name='eliminar-estudiante'),
    path('docentes/', docentes, name='docentes'),
    path('docentes/buscar', buscar_docentes, name='buscar-docentes'),
    path('docentes/', listar_docentes, name='listar-docentes'),
    path('docentes/crear/', crear_docente, name='crear-docente'),
    path('docentes/<int:pk>/', detalle_docente, name='detalle-docente'),
    path('docentes/<int:pk>/editar/', editar_docente, name='editar-docente'),
    path('docentes/<int:pk>/eliminar/', eliminar_docente, name='eliminar-docente'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
    path('estudiantes/buscar', buscar_estudiantes, name='buscar-estudiantes'),
    path('about/', about, name='about'),
    # urls con vistas basadas en clases
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
    path('editar/<int:pk>', AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>', AutoDeleteView.as_view(), name='eliminar-auto'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='detalle-curso'),
    path('curso/<int:pk>/editar/', CursoUpdateView.as_view(), name='editar-curso'),
    path('curso/<int:pk>/eliminar/', CursoDeleteView.as_view(), name='eliminar-curso'),

]
