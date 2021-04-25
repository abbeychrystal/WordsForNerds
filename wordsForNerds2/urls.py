from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookapp.urls')),
    # to use the built-in authentication for members through our new members app, need these paths (order is important) - can access built-in login and logout paths for instance:
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
