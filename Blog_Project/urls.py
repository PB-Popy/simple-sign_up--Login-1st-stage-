from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Blog_Project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage', signupPage, name= 'signupPage'),
    path("", signInPage, name="signInPage"),
    path("logoutPage", logoutPage, name="logoutPage"),
    path("homePage", homePage, name="homePage"),
    path("ProfilePage", ProfilePage, name="ProfilePage"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
