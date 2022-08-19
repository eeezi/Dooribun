from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from main import views
from chat import views as chat_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('new/', views.new, name='new'),
    path('chat/<int:post_id>', chat_views.chat, name='chat'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)