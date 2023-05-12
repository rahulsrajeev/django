from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.apps import apps

apps.check_models_ready()


def index(request):
    message = 'Welcome to the homepage!'
    count = 0
    return render(request, 'index.html', {'message': message, 'count': count})

def get_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # create a new student object and save it to the database
            s_name = form.cleaned_data['name']
            s_roll = form.cleaned_data['roll']
            s_degree = form.cleaned_data['degree']
            s_branch = form.cleaned_data['branch']
            new_student = Student(name=s_name, roll=s_roll, degree=s_degree, branch=s_branch)
            new_student.save()

            # redirect to the same page to avoid form resubmission on refresh
            return HttpResponseRedirect('/student/')
    else:
        # retrieve all the student objects from the database
        students = Student.objects.all()
        return render(request, 'index.html', {'form': StudentForm(), 'students': students})
