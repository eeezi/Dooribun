from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('chat/', include('chat.urls')),

]