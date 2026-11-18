
from utils.patient_helper import create_test_patient


def test_patch_patient(api_client):

    # Step 1: Create a Patient
    patient_id = create_test_patient(api_client)

    # Step 2: PATCH only the gender field
    patch_payload = [
        {
            "op": "replace",
            "path": "/gender",
            "value": "male"
        }
    ]

    patch_response = api_client.patch(
        f"Patient/{patient_id}",
        patch_payload,
        content_type="application/json-patch+json"
    )

    assert patch_response.status_code == 200

    # Step 3: Verify updated Patient
    get_response = api_client.get(f"Patient/{patient_id}")

    assert get_response.status_code == 200

    updated_patient = get_response.json()

    assert updated_patient["gender"] == "male"
    assert updated_patient["name"][0]["family"] == "TestFamily"

    print("Patient PATCH successful and verified!")
