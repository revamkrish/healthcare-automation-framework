
import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}/{endpoint}",
            params=params,
            headers={"Accept": "application/fhir+json"},
            timeout=20
        )

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}/{endpoint}",
            json=payload,
            headers={"Accept": "application/fhir+json"},
            timeout=20
        )

    def put(self, endpoint, payload):
        return requests.put(
            f"{self.base_url}/{endpoint}",
            json=payload,
            headers={"Accept": "application/fhir+json"},
            timeout=20
        )

    def patch(self, endpoint, payload, content_type):
        return requests.patch(
            f"{self.base_url}/{endpoint}",
            json=payload,
            headers={
                "Accept": "application/fhir+json",
                "Content-Type": content_type
            },
            timeout=20
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}/{endpoint}",
            headers={"Accept": "application/fhir+json"},
            timeout=20
        )
