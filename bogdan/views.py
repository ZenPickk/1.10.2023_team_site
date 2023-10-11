from django.shortcuts import render

# Create your views here.
def to_bogdan(request):
    return render(request, 'bogdan/bogdan.html')