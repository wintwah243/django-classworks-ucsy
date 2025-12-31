from django.shortcuts import render
from .forms import StudentForm

def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():

            data = {}

            data['username'] = form.cleaned_data['username']
            data['email'] = form.cleaned_data['email']

            # Date format
            dob = form.cleaned_data['date_of_birth']
            data['date_of_birth'] = dob.strftime('%b. %d,%Y')

            data['interests'] = form.cleaned_data['interests']

            # semester to number
            semester_map = {
                'IV': 1,
                'V': 2,
                'VI': 3
            }
            data['academic_year'] = semester_map[
                form.cleaned_data['academic_year']
            ]

            return render(request, 'list.html', data)

    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})


def list_view(request):
    data = request.session.get('data')
    return render(request, 'list.html', data)
