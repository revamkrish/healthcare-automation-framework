# to run tests - pytest tests/api/test_patient_put2.py -v -s

from utils.patient_helper import create_test_patient


def test_update_patient(api_client):

    # Step 1: Create a Patient using reusable helper
    patient_id = create_test_patient(api_client)

    # Step 2: Prepare updated Patient data
    updated_patient = {
        "resourceType": "Patient",
        "id": patient_id,
        "active": True,
        "name": [{
            "use": "official",
            "family": "UpdatedFamily",
            "given": ["UpdatedName"]
        }],
        "gender": "male",
        "birthDate": "1992-08-20"
    }

    # Step 3: Send PUT request
    update_response = api_client.put(
        f"Patient/{patient_id}",
        updated_patient
    )

    assert update_response.status_code == 200

    # Step 4: Verify updated Patient
    get_response = api_client.get(f"Patient/{patient_id}")

    assert get_response.status_code == 200

    actual_patient = get_response.json()

    assert actual_patient["name"][0]["family"] == "UpdatedFamily"
    assert actual_patient["gender"] == "male"

    print("Patient PUT successful and verified!")
