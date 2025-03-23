from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Harry Potter API! Visit /api/characters/ to see data."})

