import os
from dotenv import load_dotenv
# dotenv is a Python library that helps your application read configuration values from a .env file.
# A .env file is a simple text file containing environment variables (configuration values).

load_dotenv() # Performs the loading

ENV = os.getenv("TEST_ENV", "dev").lower() # Reads a specific environment variable

ENVIRONMENTS = {
    "dev": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    },
    "sit": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    },
    "uat": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    }
}

if ENV not in ENVIRONMENTS:
    raise ValueError(f"Invalid environment: {ENV}")

# UI application
BASE_URL = ENVIRONMENTS[ENV]["base_url"]

CURA_USERNAME = os.getenv("CURA_USERNAME")
CURA_PASSWORD = os.getenv("CURA_PASSWORD")

if not CURA_USERNAME or not CURA_PASSWORD:
    raise ValueError("CURA credentials are missing. Check your .env file.")

# API application
API_BASE_URL = "https://hapi.fhir.org/baseR4"


#ENVIRONMENTS = {
#    "dev": {
#        "base_url": "CURA UI URL",
#        "api_base_url": "HAPI FHIR API URL"
#    },
#    "qa": {
#        "base_url": "QA UI URL",
#        "api_base_url": "QA API URL"
#    }
# }
