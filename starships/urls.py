from django.urls import path, include
from . import views

urlpatterns = [
    path('x_wing', views.get_x_wing_info),
    path('imperial_shuttle', views.get_imperial_shuttle_info),
    path('droid_control_ship', views.get_droid_control_ship_info),
]
