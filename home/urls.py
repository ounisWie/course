from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create_course_page',views.create_course_page,name="create_course_page"),
    path('save_course',views.save_course,name="save_course"),
]