from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Vehicle
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json


@csrf_exempt
def upload_file(request: HttpRequest) -> JsonResponse:
    """
    Handle file upload and update or create vehicle records in the database.

    :param request: HttpRequest object containing the uploaded file.
    :return: JsonResponse indicating success or failure.
    """
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        data = json.load(file)

        for item in data:
            # Replace commas with periods in the rejection_percentage field
            if 'rejection_percentage' in item:
                item['rejection_percentage'] = item['rejection_percentage'].replace(',', '.')

            # Validate and update or create the vehicle record
            Vehicle.objects.update_or_create(
                make=item['make'],
                model=item['model'],
                model_year=item['model_year'],
                defaults={
                    'rejection_percentage': item.get('rejection_percentage', ''),
                    'reason_1': item.get('reason_1', ''),
                    'reason_2': item.get('reason_2', ''),
                    'reason_3': item.get('reason_3', '')
                }
            )
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'}, status=400)


def search(request: HttpRequest) -> JsonResponse:
    """
    Handle search requests to filter and return vehicle records.

    :param request: HttpRequest object containing the search query.
    :return: JsonResponse with the filtered vehicle data.
    """
    query = request.GET.get('query', '').strip()
    if query:
        query_parts = query.split()
        q_objects = Q()

        # Search across multiple fields
        for part in query_parts:
            q_objects &= (
                Q(make__icontains=part)
                | Q(model__icontains=part)
                | Q(model_year__icontains=part)
                | Q(rejection_percentage__icontains=part)
                | Q(reason_1__icontains=part)
                | Q(reason_2__icontains=part)
                | Q(reason_3__icontains=part)
            )

        vehicles = Vehicle.objects.filter(q_objects)[:50]
    else:
        vehicles = Vehicle.objects.all()[:50]

    serialized_vehicles = [
        {
            'make': vehicle.make,
            'model': vehicle.model,
            'model_year': vehicle.model_year,
            'rejection_percentage': vehicle.rejection_percentage,
            'reason_1': vehicle.reason_1,
            'reason_2': vehicle.reason_2,
            'reason_3': vehicle.reason_3
        } for vehicle in vehicles
    ]

    return JsonResponse(serialized_vehicles, safe=False)


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the main page with the search and upload functionality.

    :param request: HttpRequest object.
    :return: HttpResponse rendering the index.html template.
    """
    return render(request, 'index.html')
