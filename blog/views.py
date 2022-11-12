from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def blog(request):
    blg = Blog.objects.all()
    context={'blg':blg}
    return render(request,'blog.html', context)
def blogdetail(request,pk):
    blg = Blog.objects.all().order_by('date')
    data = Blog.objects.get(pk=pk)
    context={'data':data, 'blg':blg}
    return render(request, 'blogdetail.html',context)