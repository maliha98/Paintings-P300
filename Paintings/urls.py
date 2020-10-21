from django.contrib import admin
from django.urls import path
from home.views import *
from user_accounts.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('signin/', signInPage, name='signin'),
    path('logout/', logoutPage, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
