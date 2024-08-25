from django.shortcuts import render, redirect
from .models import Student, form
from django.views.generic.detail import DetailView

# Function- based view
def show_student(request, student_id):
    student = Student.objects.all(id=student_id)
    context = {'student': student}
    return render(request, 'student/show_id.html', context)

# Class-based view
# class form(DetailView):
#     model = form
#     template_name = 'student/form.html'
#     context_object_name = 'form'

def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        form = request.POST.get('form')

        # save student data
        student = Student(name=name, date_of_birth=date_of_birth, form=form)
        student.save()

        # redirect to a different page after save
        return redirect('student_detail', student_id=student.id)
    
    return render(request, 'form.html')