from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),
    path("register/", views.register, name="register"),
    
    # Рекомендуется использовать accounts/login, чтобы совпадало со стандартами Django
    path("accounts/login/", auth_views.LoginView.as_view(template_name="students/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    
    # Или можно просто подключить все стандартные пути (login, logout, password_reset) одной строкой:
    # path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
