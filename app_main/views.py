from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404

from app_users.forms import UserForm, StudentForm, BookForm
from app_users.models import Hobby, Student

User = get_user_model()


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'app_main/home.html')


def teachers(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')
    
    teachers_list = User.objects.all()

    context = {
        'teachers': teachers_list
    }

    return render(request, 'app_main/teachers.html', context)

def teacher_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            if request.POST.get('password1') == request.POST.get('password2'):
                user = form.save(commit=False)
                user.set_password(request.POST.get('password1'))
                user.save()
                return redirect('teachers')

    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'app_main/teacher_form.html', context)


def teacher_detail(request, id):
    teacher = get_object_or_404(User, id=id)
    context = {
        'teacher': teacher
    }
    return render(request, 'app_main/teacher.html', context)




def teacher_update(request, id):
    teacher = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=teacher)

        if form.is_valid() and (request.POST.get('password1') == request.POST.get('password2')):
            teacher = form.save(commit=False)
            teacher.set_password(request.POST.get('password2'))
            teacher.save()
            return redirect('teachers')
        else:
            return redirect('teacher_update', id=teacher.id)

    form = UserForm(instance=teacher)
    context = {
        'teacher': teacher,
        'form': form
    }
    return render(request, 'app_main/teacher_form.html', context)


def teacher_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('teachers')


def students_list(request, id):
    teacher = get_object_or_404(User, id=id)
    students = teacher.student_set.all()

    context = {
        'students': students,
        'teacher': teacher,
    }
    return render(request, 'app_main/students.html', context)

def student_create(request, teacher_id):
    teacher = get_object_or_404(User, id=teacher_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.fields.pop('hobbies', None)

        if form.is_valid():
            student = form.save(commit=False)
            student.teacher = teacher
            student.save()
            
            return redirect('teacher_students', id=teacher_id)


    form = StudentForm()
    form.fields.pop('hobbies', None)

    context = {
        'form': form,
        'btn_text': 'Create student',
        'btn_color': 'green-600',
        'title': 'New student',
    }
    return render(request, 'app_main/student_form.html', context)


def student_update(request, student_id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if not request.user.is_superuser:
        return redirect('teachers')

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('teacher_students', id=student.teacher.id)

    form = StudentForm(instance=student)
    context = {
        'form': form,
        'btn_text': 'Update student',
        'btn_color': 'yellow-600'
    }
    return render(request, 'app_main/student_form.html', context)


def filter_students(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id)
    students = []

    for student in Student.objects.all():
        if hobby in student.hobbies.all():
            students.append(student)
    context = {
        'hobby_name': hobby.name, 
        'students': students,
    }
    return render(request, 'app_main/filtered_students.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,   
    }
    return render(request, 'app_main/student_detail.html', context)


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    student.delete()
    return redirect('teacher_students', id=student.teacher.id)  

def book_create(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save(commit=False)  
            book.student = student  
            book.save()
            return redirect('teacher_students', id=student.teacher.id)

    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'app_main/book_create.html', context)