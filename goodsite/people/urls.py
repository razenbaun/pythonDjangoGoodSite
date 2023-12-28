from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('privacy/', privacy, name='privacy'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/delete/', delete_portfolio, name='delete_portfolio'),
    path('addportfolio/', add_portfolio, name='add_portfolio'),
    path('addachievement/', add_achievement, name='add_achievement'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<slug:portfolio_slug>/', show_portfolio, name='portfolio_slug'),
    path('portfolio/<slug:portfolio_slug>/<slug:cat_slug>/', portfolio_cat, name='portfolio_cat'),
    path('profile/', profile, name='profile'),
    path('profile/<slug:cat_slug>/', profile_cat, name='profile_cat'),
    path('home/', redirect_to_home, name='home_redirect'),
]
