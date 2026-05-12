from django.db import models


# Модель группы (необходима для Student)
class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель клуба (необходима для Student)
class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Объединенная модель студента
class Student(models.Model):
    # Поля из первой версии
    first_name = models.CharField(max_length=110)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    # Поля из второй версии
    clubs = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

