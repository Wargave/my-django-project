from django.urls import path
from . import views

urlpatterns = [
    # Теперь этот путь будет открываться по адресу /students/
    path('', views.student_list, name='student_list'),
    
    # Этот по адресу /students/add/
    path('add/', views.add_student, name='add_student'),
    
    # Этот по адресу /students/1/
    path('<int:pk>/', views.student_detail, name='student_detail'),
    
    # Этот по адресу /students/1/edit/
    path('<int:pk>/edit/', views.edit_student, name='edit_student'),
    
    # Этот по адресу /students/1/delete/
    path('<int:pk>/delete/', views.delete_student, name='delete_student'),
    
    path('logout/', views.logout_view, name='logout'),
]

