from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_portfolio, name='delete_portfolio'),
    path('addportfolio/', add_portfolio, name='add_portfolio'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<slug:portfolio_slug>/', show_portfolio, name='portfolio_slug'),
    path('home/', redirect_to_home, name='home_redirect'),
]
