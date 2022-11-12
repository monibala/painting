from login import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path,include

from login.forms import MyPasswordRestForm, MySetPasswordForm

# from .forms import LoginForm , MyPasswordChangeForm,MyPasswordRestForm,MySetPasswordForm
urlpatterns = [
#    path('login/', auth_views.LoginView.as_view(template_name='login.html' , authentication_form = LoginForm ),name='login'),
   path('login/', views.login_user, name='login'),
   path('registration/', views.register, name='registration'),
   path('profile/', views.Profile, name='profile'),
   path('address/', views.address, name='address'),
   path('passwordchangedone',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
   path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordRestForm),name='password_reset'),
   path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
   path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
   path('forgot', views.forgot, name='forgot'),
   path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout',),
   path('change_password/', views.change_password, name='change_password'),
]
