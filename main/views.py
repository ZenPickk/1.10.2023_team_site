from django.shortcuts import render

# Create your views here.
def to_main(request):
    return render(request, 'main/main.html')