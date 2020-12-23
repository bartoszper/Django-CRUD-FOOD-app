
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('register/',user_views.register, name = 'register'),
    path('login/', authentication_view.LoginView.as_view(), name = 'login')
]
