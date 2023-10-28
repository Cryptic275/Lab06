from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Course, Student

# Create your views here.

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


def courses(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, template_name="labApp/courses.html",
                  context={"courses": Course.objects.all(), "form": CourseModelForm()})


def students(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, template_name="labApp/students.html",
                  context={"students": Student.objects.all(), "form": StudentModelForm()})


def details(request, studentId):
    student = Student.objects.get(studentID=studentId)
    unregisteredCourses = Course.objects.exclude(students=student).all()

    if request.method == "POST":
        courseId = request.POST["course"]
        course = Course.objects.get(courseID=courseId)
        student.courses.add(course)

    return render(request, template_name='labApp/index.html', context={
        "student": student,
        "unregisteredCourses": unregisteredCourses,
    })