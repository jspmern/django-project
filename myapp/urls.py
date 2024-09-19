from . import views
from django.urls import path,include
urlpatterns = [
      path("",views.RegisterPage,name="registration"),
      path('register/',views.RegistarationHandler,name="register")
      path('login/',views.)
]