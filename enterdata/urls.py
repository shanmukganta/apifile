from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    path('success/',views.home,name='success'),
    path('fetch/',views.fetch,name='fetch'),

]
