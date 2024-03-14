from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from  clinic import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("doctors",views.DoctorView,basename="doctors_list")
router.register("appointments",views.AppointmentView,basename="appointments_list")

urlpatterns = [    
    path("register/",views.UserCreateView.as_view(),name="signup"),
    path("login/",ObtainAuthToken.as_view(),name="token"),
    path("profile/",views.ProfileView.as_view(),name="profile"),

] +router.urls