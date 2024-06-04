import pytest
from django.urls import reverse
from vehicles.models import Vehicle
from django.core.files.uploadedfile import SimpleUploadedFile
import json


@pytest.mark.django_db
def test_upload_file(client):
    """
    Test the file upload functionality.

    This test checks if the file upload endpoint correctly handles a POST request
    with a JSON file, processes the data, and updates or creates vehicle records
    in the database.

    Steps:
    1. Create a JSON file with vehicle data.
    2. Upload the file to the 'upload_file' endpoint.
    3. Verify the response status and content.
    4. Check if the vehicle data is correctly stored in the database.
    """
    url = reverse('upload_file')
    data = [
        {
            "model_year": "2020",
            "make": "Toyota",
            "model": "Corolla",
            "rejection_percentage": "0.5%",
            "reason_1": "Engine",
            "reason_2": "Brakes",
            "reason_3": "Suspension"
        }
    ]
    json_data = json.dumps(data).encode('utf-8')
    file = SimpleUploadedFile('test.json', json_data, content_type='application/json')

    response = client.post(url, {'file': file})
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}

    # Verify data in the database
    vehicle = Vehicle.objects.get(make='Toyota')
    assert vehicle.model_year == '2020'
    assert vehicle.make == 'Toyota'
    assert vehicle.model == 'Corolla'
    assert vehicle.rejection_percentage == '0.5%'
    assert vehicle.reason_1 == 'Engine'
    assert vehicle.reason_2 == 'Brakes'
    assert vehicle.reason_3 == 'Suspension'


@pytest.mark.django_db
def test_search_vehicles(client):
    """
    Test the search functionality.

    This test checks if the search endpoint correctly handles GET requests and
    returns filtered vehicle data based on the query parameters.

    Steps:
    1. Create test vehicle data in the database.
    2. Test the search functionality with a specific query.
    3. Verify the response status and content for the query.
    4. Test the search functionality without any query.
    5. Verify the response status and content for the no-query case.
    """
    # Create test data
    Vehicle.objects.create(
        model_year='2020',
        make='Toyota',
        model='Corolla',
        rejection_percentage='0.5%',
        reason_1='Engine',
        reason_2='Brakes',
        reason_3='Suspension'
    )

    Vehicle.objects.create(
        model_year='2019',
        make='Honda',
        model='Civic',
        rejection_percentage='0.3%',
        reason_1='Transmission',
        reason_2='Brakes',
        reason_3='Electrical'
    )

    # Test search functionality
    url = reverse('search')

    # Test with query
    response = client.get(url, {'query': 'Toyota'})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['make'] == 'Toyota'
    assert data[0]['model'] == 'Corolla'

    # Test without query
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
