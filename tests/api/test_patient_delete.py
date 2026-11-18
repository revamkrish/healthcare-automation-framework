
from utils.patient_helper import create_test_patient


def test_delete_patient(api_client):

     # Step 1: Create a Patient
    patient_id = create_test_patient(api_client)

    # Step 2: Delete Patient
    delete_response = api_client.delete(f"Patient/{patient_id}")

    assert delete_response.status_code in (200, 204)

    print(f"Patient {patient_id} deleted successfully!")

    # Step 3: Verify deletion
    get_response = api_client.get(f"Patient/{patient_id}")

    assert get_response.status_code in (404, 410)

    print("Patient deletion verified!")
