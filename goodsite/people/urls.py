from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('object_types/', object_types, name='object_types'),
    path('about/', about, name='about'),
    path('pri/', pri_group, name='pri_group'),
    path('pri/<int:number_student>/', pri_id, name='spisok_pri'),
    path('pri/<slug:cat>/', categories, name='categories'),
    path('post/', post_detail, name="post_detail"),
    path('home/', redirect_to_home, name='home_redirect'),
    path('split/<str:line>/<str:sepp>/', split_line, name='split_line'),
    path('filters/', filters, name='filters'),
]