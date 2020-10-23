from django.shortcuts import render
from backend.models import Champion

def index(request):
    # Champion.process_specific_champion("Aatrox")
    return render(request, 'frontend/index.html')