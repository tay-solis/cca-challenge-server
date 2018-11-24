from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_sections, name='all_sections'),
    path('section/<int:pk>/upvote', views.section_register, name='section_register'),
    path('section/<int:pk>/downvote', views.section_drop, name='section_drop'),
    path('section/<int:pk>', views.section_detail, name='section_detail'),
    
]