
def get_patient_payload(unique_id):

    patient_payload = {
        "resourceType": "Patient",
        "identifier": [{
            "system": "https://example.org/patient-id",
            "value": unique_id
        }],
        "active": True,
        "name": [{
            "use": "official",
            "family": "TestFamily",
            "given": ["API"]
        }],
        "gender": "female",
        "birthDate": "1990-05-15"
    }

    return patient_payload
