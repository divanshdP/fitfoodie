
# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^$', app.views.home , name='home'),
    path('home/', app.views.home , name='home'),
    path('about/', app.views.about , name='about'),
    path('menu/', app.views.menu, name='menu'),
    path('menu/burgers/', app.views.burgers , name='burgers'),
    path('menu/drinks/', app.views.drinks , name='drinks'),
    path('menu/sweets/', app.views.sweets , name='sweets'),
    path('menu/pizzas/', app.views.pizzas , name='pizzas'),
    path('restaurants/', app.views.restaurants, name='restaurants'),
    path('restaurants/menu/' , app.views.menu , name='restmenu'),
    path('restaurants/menu/<str:cat>/' , app.views.restwise , name='restwise'),
    path('menu/addtocart/<int:id>', app.views.addtocart , name='addtocart'),
    path('gallery/', app.views.gallery, name='gallery'),
    path('login/', app.views.login, name='login'),
    path('signup/', app.views.signup, name='signup'),
    path('userprofile/', app.views.login , name='userprofile'),
    path('lastorders/' , app.views.lastorders , name='lastorders'),
    path('logout/', app.views.logout , name ='logout'),
    path('feedback/', app.views.mail , name='feedback'),
    path('cart/', app.views.showCart, name='cart'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)