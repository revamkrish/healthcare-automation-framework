
import uuid
from test_data.patient_data import get_patient_payload


def create_test_patient(api_client):

    # Step 1: Generate unique identifier
    unique_id = str(uuid.uuid4())

    # Step 2: Get Patient payload from test data
    patient_payload = get_patient_payload(unique_id)

    # Step 3: Create Patient using API client
    response = api_client.post("Patient", patient_payload)

    assert response.status_code == 201, (
        f"Patient creation failed: {response.status_code} - {response.text}"
    )

    # Step 4: Extract Patient ID
    patient_id = response.json()["id"]

    print(f"Test Patient created: {patient_id}")

    return patient_id
