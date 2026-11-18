
from utils.patient_helper import create_test_patient


def test_create_patient(api_client):

    # Step 1: Create a Patient
    patient_id = create_test_patient(api_client)

    # Step 2: Get Patient
    get_response = api_client.get(f"Patient/{patient_id}")

    assert get_response.status_code == 200

    patient = get_response.json()

    print(patient)
