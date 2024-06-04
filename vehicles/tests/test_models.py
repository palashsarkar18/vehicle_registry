import pytest
from vehicles.models import Vehicle


@pytest.mark.django_db
def test_vehicle_model():
    """
    Test the Vehicle model.

    This test checks if the Vehicle model correctly stores and retrieves data.

    Steps:
    1. Create a Vehicle instance with test data.
    2. Verify that the data is correctly saved in the database.
    3. Retrieve the vehicle from the database and check if the data matches the test data.
    """
    # Create a Vehicle instance with test data
    vehicle = Vehicle.objects.create(
        model_year='2020',
        make='Toyota',
        model='Corolla',
        rejection_percentage='0.5%',
        reason_1='Engine',
        reason_2='Brakes',
        reason_3='Suspension'
    )

    # Verify that the data is correctly saved in the database
    assert vehicle.model_year == '2020'
    assert vehicle.make == 'Toyota'
    assert vehicle.model == 'Corolla'
    assert vehicle.rejection_percentage == '0.5%'
    assert vehicle.reason_1 == 'Engine'
    assert vehicle.reason_2 == 'Brakes'
    assert vehicle.reason_3 == 'Suspension'

    # Retrieve the vehicle from the database and check if the data matches the test data
    saved_vehicle = Vehicle.objects.get(id=vehicle.id)
    assert saved_vehicle.model_year == '2020'
    assert saved_vehicle.make == 'Toyota'
    assert saved_vehicle.model == 'Corolla'
    assert saved_vehicle.rejection_percentage == '0.5%'
    assert saved_vehicle.reason_1 == 'Engine'
    assert saved_vehicle.reason_2 == 'Brakes'
    assert saved_vehicle.reason_3 == 'Suspension'
