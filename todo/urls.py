from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),  # Include the todo app's URLs under the 'api/' path
]
