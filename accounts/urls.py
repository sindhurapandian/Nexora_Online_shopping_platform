from django.urls import path
from . import views

urlpatterns =[
    path('register_view/',views.register_view,name='register_view'),
    path('login_view/',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
]