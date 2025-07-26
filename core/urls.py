
from django.contrib import admin
from django.urls import path
from home.views import home,about,contact
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vegies.views import *


urlpatterns = [
    path('',home,name="home"),
    path('recepies/',recepies,name="recepies"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('admin/', admin.site.urls),
    path('delete_recepie/<id>/',delete_recepie,name="delete_recepie"),
    path('update_recepie/<id>/',update_recepie,name="update_recepie"),
    path('f_recepies',f_recepies,name="f_recepies"),
    path('delete_recepies/<id>/',delete_recepies,name="delete_recepies"),
    path('update_recepies/<id>/',update_recepies,name="update_recepies"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()