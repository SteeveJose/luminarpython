from django.contrib import admin
from django.urls import path, include

from medclapp.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register, name='register'),
    path('medclapp/',include("medclapp.urls")),

]