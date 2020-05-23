
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^account/', include('account.urls')),
# ]


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]