from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    #Auth
    path('accounts/', include('allauth.urls')),

    #Vidz
    path('', include('home.urls'))
]

admin.site.site_header = "boticstube"
admin.site.site_title = "boticstube Admin Portal"
admin.site.index_title = "boticstube Admin"

