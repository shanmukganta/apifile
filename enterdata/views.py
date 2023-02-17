from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post

def home(request):
        return render(request,'success.html')
def create(request):
        
        if request.method == 'POST':
        
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                return HttpResponseRedirect('success/')
                  
                
        else:
                return render(request,'createpost.html')


# Create your views here.
def fetch(request):
        data=Post.objects.all()
        #tit= {"Title":data}
        return render(request, "fetch.html",{'name':data})