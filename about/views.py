from django.shortcuts import render

from category.models import category_types

# Create your views here.
def about(request):
    cat = category_types.objects.all()
    context = {'cat':cat}
    return render(request, 'about.html', context)