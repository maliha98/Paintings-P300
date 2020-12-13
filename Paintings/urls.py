from django.contrib import admin
from django.urls import path
from home.views import *
from user_accounts.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('signin/', signInPage, name='signin'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signUpPage, name='signup'),
    path('cart/', cartView, name='cart'),
    path('cart/<id>', addToCart, name='cart'),
    path('<id>', plusCart, name='pluscart'),
    path('minus/<id>', minusCart, name='minuscart'),
    path('remove/<id>', removeCart, name='removecart'),
    path('catgory/<id>', categoryView, name='category'),
    path('checkout/', checkout, name='checkout'),
    path('address_update/<id>', address_form, name='address_update'),
    path('payment/', payment, name='payment'),
    path('about/', aboutPage, name='about'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
