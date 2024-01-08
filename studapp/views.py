from django.shortcuts import render, redirect
from .import views 
from studapp.models import Student
# Create your views here.

def redirect_to_students(request):
    return redirect('show_students')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        joining_date = request.POST.get('joining_date')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            joining_date=joining_date,
            qualification=qualification,
            gender=gender,
            mobile_number=mobile_number,
            address=address
        )

        return redirect('show_students')

    return render(request, "add_student.html")


def show_students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})

def student_details(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, "student_details.html", {"student": student})

def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, "edit_student.html", {"student": student})

def update_student(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.joining_date = request.POST.get('joining_date')
        student.qualification = request.POST.get('qualification')
        student.gender = request.POST.get('gender')
        student.mobile_number = request.POST.get('mobile_number')
        student.address = request.POST.get('address')
        student.save()
        return redirect('show_students')

    return render(request, "edit_student.html", {"student": student})


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('show_students')
