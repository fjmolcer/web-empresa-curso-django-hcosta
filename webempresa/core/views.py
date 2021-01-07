from django.shortcuts import render


# Create your views here.
def home(request):
    """Renderiza la págiona de Home"""
    return render(request, 'core/home.html')

def about(request):
    """Renderiza la págiona de About"""
    return render(request, 'core/about.html')

def store(request):
    """Renderiza la págiona de Store"""
    return render(request, 'core/store.html')
    