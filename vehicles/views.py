import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Vehicle
from .serializers import VehicleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        data = json.load(file)
        for item in data:
            vehicle, created = Vehicle.objects.update_or_create(
                make=item['make'],
                model=item['model'],
                model_year=item['model_year'],
                defaults=item
            )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})


def search(request):
    query = request.GET.get('query', '')
    if query:
        vehicles = Vehicle.objects.filter(
            Q(make__icontains=query) |
            Q(model__icontains=query) |
            Q(model_year__icontains=query)
        )[:50]
    else:
        vehicles = Vehicle.objects.all()[:50]
    serializer = VehicleSerializer(vehicles, many=True)
    return JsonResponse(serializer.data, safe=False)


def index(request):
    return render(request, 'index.html')
