from django.contrib import admin

from myApp.models import *

admin.site.register (CustomUser)
admin.site.register(viewersProfileModel) 
admin.site.register(BloggerProfileModel) 
