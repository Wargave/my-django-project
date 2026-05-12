from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, include
from students import views
from django.conf.urls.static import static
from django.contrib import admin

# Определяем основной список путей
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="students/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]

# Добавляем статику и медиа, только если DEBUG = True (в режиме разработки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)