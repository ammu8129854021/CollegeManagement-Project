from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('add_student', views.add_student, name='add_student'),
    path('show_students', views.show_students, name='show_students'),
    path('student_details/<int:pk>', views.student_details, name='student_details'),
    path('edit_student/<int:pk>', views.edit_student, name='edit_student'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
]
