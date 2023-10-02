from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('pri/', pri_group),
    path('pri/<int:number_student>/', pri_id),
    path('pri/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', DateProcessing.archive),
]