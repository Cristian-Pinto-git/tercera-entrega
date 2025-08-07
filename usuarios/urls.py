from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, CustomLoginView, CustomLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView, editar_usuario, eliminar_usuario

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("profile/edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    path('update-avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
    #path('usuarios/', usuarios, name='usuarios'),
    path('editar/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('cambiar-password/', auth_views.PasswordChangeView.as_view(template_name='usuarios/cambiar_password.html', 
    success_url='/usuarios/profile/'), name='cambiar_password'),
    #path('password-cambiado/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_cambiado.html'), name='password_cambiado'),
]
