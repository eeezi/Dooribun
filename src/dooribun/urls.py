from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:chat_id>', views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)