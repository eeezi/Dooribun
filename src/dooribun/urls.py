from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('chat/', include('chat.urls')),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout')
]