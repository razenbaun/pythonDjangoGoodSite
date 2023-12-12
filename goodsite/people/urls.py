from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<int:portfolio_id>/', show_portfolio, name='portfolio_id'),
    path('portfolio/<slug:cat>/', categories, name='categories'),
    path('home/', redirect_to_home, name='home_redirect'),
]
