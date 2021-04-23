from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('submit',views.submit_login ),
    path('register/',views.register, name='register'),
    path('sucess/',views.success, name='sucess'),
]