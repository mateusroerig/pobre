from django.urls import path

from .views import SignUpView, UsuarioUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('update-user-info/', UsuarioUpdateView.as_view(), name='update_user_info'),
]
