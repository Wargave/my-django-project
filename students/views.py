from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout  # Импорт должен быть здесь
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student, Group, Club
from .forms import RegisterForm


# 1. Список студентов
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})


# 2. Добавление студента
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        group_id = request.POST.get("group")
        photo = request.FILES.get("photo")
        selected_clubs_ids = request.POST.getlist('clubs')

        # Создаем студента
        group_obj = Group.objects.get(pk=group_id)
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            group=group_obj,
            photo=photo
        )

        # Привязываем кружки
        student.clubs.set(selected_clubs_ids)

        return redirect("student_list")

    context = {
        'groups': Group.objects.all(),
        'clubs': Club.objects.all()
    }
    return render(request, "students/add_student.html", context)


# 3. Детали студента
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})


# 4. Редактирование студента
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.age = request.POST.get("age")

        # Обновляем группу
        group_id = request.POST.get("group")
        student.group = Group.objects.get(pk=group_id)

        # Обновляем кружки
        selected_clubs_ids = request.POST.getlist('clubs')
        student.clubs.set(selected_clubs_ids)

        if request.FILES.get("photo"):
            student.photo = request.FILES.get("photo")

        student.save()
        return redirect("student_list")

    context = {
        'student': student,
        'groups': Group.objects.all(),
        'clubs': Club.objects.all()
    }
    return render(request, "students/edit_student.html", context)


# 5. Удаление студента
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")


# 6. Регистрация
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "students/register.html", {"form": form})


# 7. Функция выхода
def logout_view(request):
    logout(request)
    return redirect('login')