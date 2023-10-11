from django.shortcuts import render

# Create your views here.
def to_danylo(request):
    return render(request, 'danylo/danylo.html')