from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .forms import StudentForm
from .model import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    return render(request, 'index.html',context=context)