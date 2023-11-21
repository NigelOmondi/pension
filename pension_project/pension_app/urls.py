from django.urls import path
from .views import home, user_list, search_user, change_status

urlpatterns = [
    path('', home, name="home"),
    path('users/', user_list, name='user_list'),
    path('search/', search_user, name='search_user'),
    path('change-status/', change_status, name='change_status_no_arg'),
    path('change-status/<str:pension_number>/', change_status, name='change_status'),
]
