
def test_get_patients(api_client):

    response = api_client.get(
        "Patient",
        params={"_count": 5}
    )

    # Verify response status
    assert response.status_code == 200

    response_data = response.json()

    # Verify response structure
    assert response_data["resourceType"] == "Bundle"
    assert response_data["type"] == "searchset"

    patients = response_data.get("entry", [])

    assert len(patients) > 0

    print(f"\nTotal patients returned: {len(patients)}")

    # Print patient details
    for item in patients:
        patient = item["resource"]

        patient_id = patient.get("id")
        gender = patient.get("gender")
        birth_date = patient.get("birthDate")

        names = patient.get("name", [])

        if names:
            family_name = names[0].get("family", "")
            given_names = names[0].get("given", [])
            first_name = " ".join(given_names)
            full_name = f"{first_name} {family_name}".strip()
        else:
            full_name = "Name not available"

        print(f"\nPatient ID : {patient_id}")
        print(f"Name       : {full_name}")
        print(f"Gender     : {gender}")
        print(f"Birth Date : {birth_date}")
