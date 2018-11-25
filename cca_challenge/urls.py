from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_sections, name='all_sections'),
    path('<int:id>/register', views.section_register, name='section_register'),
    path('<int:id>/drop', views.section_drop, name='section_drop'),
    
]