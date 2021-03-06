from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('jobs.urls', namespace='jobs')),
]


