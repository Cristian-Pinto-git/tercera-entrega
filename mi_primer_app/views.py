from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Curso, Docente, Estudiante, Auto

from .forms import CursoForm, DocenteForm, EstudianteForm, AutoForm

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_docente(request):
   
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el docente
            nuevo_docente = Docente(
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            email=form.cleaned_data['email'],
            edad=form.cleaned_data['edad'],
            )
            nuevo_docente.save()
        return redirect('inicio')
    else:
        form = DocenteForm()
        return render(request, 'mi_primer_app/crear_docente.html', {'form': form})


def crear_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                docente=form.cleaned_data['docente'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear_curso.html', {'form': form})


def crear_estudiante(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el estudiante
            nuevo_estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                curso = form.cleaned_data['curso'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_estudiante.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
    
    return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes})

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'mi_primer_app/docentes.html', {'docentes': docentes})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre': nombre})

def buscar_docentes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        docentes = Docente.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/docentes.html', {'docentes': docentes, 'nombre': nombre})
    
def buscar_estudiantes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes, 'nombre': nombre})


class AutoListView(ListView):
    model = Auto
    template_name = 'mi_primer_app/listar_autos.html'
    context_object_name = 'autos'
    

class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'mi_primer_app/detalle_auto.html'
    context_object_name = 'auto'

class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'mi_primer_app/eliminar_auto.html'
    success_url = reverse_lazy('listar-autos')
    
