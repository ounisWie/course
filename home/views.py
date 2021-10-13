from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Categories,Course

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def create_course_page(request):
    cat = Categories.objects.all()
    context ={"category":cat}
    return render(request,"pages/add-course.html",context)

def save_course(request):
    if request.method == "POST":
        title = request.POST.get('title')
        cat = request.POST.get('category')
        category = Categories.objects.get(name=cat)
        
        level = request.POST.get('course_level')
        desc = request.POST.get('desc')
        video_url = request.POST.get('video_url')
        image=request.FILES.get('image')
        x = Course.objects.create(title = title,category = category,course_level = level,description = desc,image = image,video_link = video_url)
        x.save()
        print(title,category,level,desc,video_url,image)
        return redirect("create_course_page")
    else:
        return HttpResponse("Babe you broke something")
    
    