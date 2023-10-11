from django.shortcuts import render

# Create your views here.
def to_rinat(request):
    return render(request, 'rinat/rinat.html')