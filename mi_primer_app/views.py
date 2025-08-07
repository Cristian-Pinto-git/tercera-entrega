from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Docente
from .forms import DocenteForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Curso, Docente, Estudiante, Auto

from .forms import CursoForm, DocenteForm, EstudianteForm, AutoForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


@login_required
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


@login_required
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


@login_required
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
            return redirect('estudiantes')
    else:
        form = EstudianteForm()
    
    return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})


@login_required
def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes})

@login_required
def detalle_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    return render(request, 'mi_primer_app/detalle_estudiante.html', {'estudiante': estudiante})

@login_required
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.apellido = form.cleaned_data['apellido']
            estudiante.email = form.cleaned_data['email']
            estudiante.edad = form.cleaned_data['edad']
            estudiante.curso = form.cleaned_data['curso']
            # fecha_inscripcion normalmente no se edita porque es auto_now_add
            estudiante.save()
            return redirect('estudiantes')
    else:
        form = EstudianteForm(initial={
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'email': estudiante.email,
            'edad': estudiante.edad,
            'curso': estudiante.curso,
            'fecha_inscripcion': estudiante.fecha_inscripcion,
        })

    return render(request, 'mi_primer_app/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

@login_required
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiantes')

    return render(request, 'mi_primer_app/eliminar_estudiante.html', {'estudiante': estudiante})


@login_required
def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'mi_primer_app/docentes.html', {'docentes': docentes})


@login_required
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})


@login_required
def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre': nombre})


@login_required
def buscar_docentes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        docentes = Docente.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/docentes.html', {'docentes': docentes, 'nombre': nombre})
    
def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'mi_primer_app/listar_docentes.html', {'docentes': docentes})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            Docente.objects.create(**form.cleaned_data)
            return redirect('listar-docentes')
    else:
        form = DocenteForm()
    return render(request, 'mi_primer_app/crear_docente.html', {'form': form})

def detalle_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    return render(request, 'mi_primer_app/detalle_docente.html', {'docente': docente})

def editar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            for campo, valor in form.cleaned_data.items():
                setattr(docente, campo, valor)
            docente.save()
            return redirect('listar-docentes')
    else:
        form = DocenteForm(initial={
            'nombre': docente.nombre,
            'apellido': docente.apellido,
            'email': docente.email,
            'edad': docente.edad,
            'curso': docente.curso,
        })
    return render(request, 'mi_primer_app/editar_docente.html', {'form': form, 'docente': docente})

def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('listar-docentes')
    return render(request, 'mi_primer_app/eliminar_docente.html', {'docente': docente})

 
@login_required   
def buscar_estudiantes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes, 'nombre': nombre})

def about(request):
    return render(request, 'mi_primer_app/about.html')


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


class CursoListView(ListView):
    model = Curso
    template_name = 'mi_primer_app/cursos.html'
    context_object_name = 'cursos'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'mi_primer_app/detalle_curso.html'

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nombre', 'descripcion', 'docente', 'duracion_semanas', 'fecha_inicio', 'activo']
    template_name = 'mi_primer_app/editar_curso.html'
    success_url = '/cursos/'

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'mi_primer_app/eliminar_curso.html'
    success_url = '/cursos/'

