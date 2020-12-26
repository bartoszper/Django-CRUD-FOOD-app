
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('register/',user_views.register, name = 'register'),
    path('login/', authentication_view.LoginView.as_view(template_name='login.html'), name = 'login'),
#    path('logout/', authentication_view.LoginView.as_view(template_name='logout.html'), name = 'logout'),
    path('logout/', user_views.logout, name = 'logout'),
    path('profile/', user_views.profilepage, name = 'profile')
]  
