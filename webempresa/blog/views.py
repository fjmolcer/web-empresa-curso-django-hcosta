from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    pots = Post.objects.all()
    return render(request, 'blog/blog.html', {'pots': pots})

def category(request, category_id):
    categorie = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category':categorie})
    