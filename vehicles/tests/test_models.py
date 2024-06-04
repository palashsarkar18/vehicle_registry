import pytest
from vehicles.models import Vehicle


@pytest.mark.django_db
def test_vehicle_model():
    vehicle = Vehicle.objects.create(
        model_year='2020',
        make='Toyota',
        model='Corolla',
        rejection_percentage='0.5%',
        reason_1='Engine',
        reason_2='Brakes',
        reason_3='Suspension'
    )
    assert vehicle.model_year == '2020'
    assert vehicle.make == 'Toyota'
    assert vehicle.model == 'Corolla'
    assert vehicle.rejection_percentage == '0.5%'
    assert vehicle.reason_1 == 'Engine'
    assert vehicle.reason_2 == 'Brakes'
    assert vehicle.reason_3 == 'Suspension'
