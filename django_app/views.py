from django.http import HttpResponse, JsonResponse
import socket

def health_check(request):
    return HttpResponse("OK")

def home(request):
    return HttpResponse(f"Hello from Pod: {socket.gethostname()}")
