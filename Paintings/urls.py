from django.contrib import admin
from django.urls import path
from home.views import homeView, profileView, aboutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('profile/', profileView),
    path('about/', aboutView,name='about'),   
]