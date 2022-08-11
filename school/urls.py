from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('studentApp/', include('studentApp.urls')),
    path('admin/', admin.site.urls),
]