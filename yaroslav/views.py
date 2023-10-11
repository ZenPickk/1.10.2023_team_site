from django.shortcuts import render

# Create your views here.
def to_yaroslav(request):
    return render(request, 'yaroslav/yaroslav.html')