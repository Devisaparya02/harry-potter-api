from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the Harry Potter API! Visit /api/characters/ to see data."})

urlpatterns = [
    path('', home_view),  # Home route
    path('admin/', admin.site.urls),
    path('api/', include('characters.urls')),
]
