import pytest
import httpx
import os
import base64
import json
from dotenv import load_dotenv

# Load environment variables from .env.test file
load_dotenv(dotenv_path='.env.test')

BASE_URL = os.getenv("BASE_URL")
VALID_USER_ID = os.getenv("VALID_USER_ID")
INVALID_USER_ID = os.getenv("INVALID_USER_ID")

# Parameters for testing
parameter = {
    "id": 2,
    "owner": "Essencif.AI",
    "prompt": "untersuche das unternehmen MICROSOFT CORP auf die Frage Nutze die ausgewählten Quellen, um damit eine detaillierte SWOT Analyse fuer das Unternehmens im aktuellen Marktumfeld zu machen. Strukturiere die Antwort so, dass du die 4 Abschnitte \"1. Stärken\", \"2. Schwächen\", \"3. Chancen\" und \"4. Risiken\" jeweils mit der ueberschrift beginnst. Nutze fuer die Ausformulierung der Bereiche eine beschreibende Textform und sei dabei möglichst präzise. Die Texte sollen pro Bereich nicht länger als 2000 Zeichen sein. Gebe für jeden Bereich bis zu drei Quellenverweise an. Zitiere dabei so, dass du das Dokument nennst und eine Seitenzahl angibst oder dass du eine Webseite als Referenz angibst.",
    "promptname": "SWOT (Text, 2000 Zeichen)",
    "engine": "gpt-4o",
    "frequency_penalty": 0.25,
    "max_tokens": 4000,
    "n": 1,
    "parameterset": "GPT 4o (Temp 1, top 0,85, pres 0,25, freq 0,25)",
    "presence_penalty": 0.25,
    "stream": False,
    "temperature": 1,
    "top_p": 0.85,
    "user": "Essencifai"
}
project_test_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',  '..'))
TEST_PDF_PATH = os.path.join(project_test_dir,  'assets/test_annual_report.pdf')

print(TEST_PDF_PATH, "test_document_analysis_gpt_knowledge")

def encode_pdf(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

@pytest.mark.asyncio
async def test_document_analysis_gpt_knowledge():
    # Prepare the payload to match the curl request
    payload = {
        "context": "Du bist ein Vertriebsmitarbeiter eines Asset Managers und möchtest den Verkaufsprozess unterstützen, indem möglichst prägnante und überzeugende Analysen für die Kunden erstellt werden.",
        "prompt": parameter,
        "analysis_type": "gpt_knowledge",
        "pdf_file": None,
        "file_name": None,
        "link": None,
        "company_name": "MSFT"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/document_analysis', json=payload, headers=headers)

        # print("Response Status:", response.status_code)
        # print("Response Text:", response.text)  # Print full error message from the backend
        assert response.status_code == 200, f"Unexpected status {response.status_code}: {response.text}"
        print(response.text)
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], str)

@pytest.mark.asyncio
async def test_document_analysis_report():
    try:
        # Encode the PDF file to base64
        base64_pdf = encode_pdf(TEST_PDF_PATH)

        # Define the payload with the base64 PDF file
        payload = {
            "context": "Du bist ein Vertriebsmitarbeiter eines Asset Managers und möchtest den Verkaufsprozess unterstützen, indem möglichst prägnante und überzeugende Analysen für die Kunden erstellt werden.",
            "prompt": parameter,
            "analysis_type": "document",
            "pdf_file": base64_pdf,
            "file_name": "test_annual_report.pdf",
            "link": None,
            "company_name": "MSFT"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
        }

        # Send the POST request
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(f'{BASE_URL}/api/document_analysis', json=payload, headers=headers)

        # print("Response Status:", response.status_code)
        # print("Response Text:", response.text)  # Print full error message from the backend
        assert response.status_code == 200, f"Unexpected status {response.status_code}: {response.text}"
        print(response.text)
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], str)

    except httpx.ReadTimeout as e:
        pytest.fail(f"Request timed out: {e}")


@pytest.mark.asyncio
async def test_document_analysis_sec_filing():
    # Prepare the payload to match the curl request
    payload = {
        "context": "Du bist ein Vertriebsmitarbeiter eines Asset Managers und möchtest den Verkaufsprozess unterstützen, indem möglichst prägnante und überzeugende Analysen für die Kunden erstellt werden.",
        "prompt": parameter,
        "analysis_type": "sec_filing",
        "pdf_file": None,
        "file_name": None,
        "link": None,
        "company_name": "MSFT"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post(f'{BASE_URL}/api/document_analysis', json=payload, headers=headers)

        # print("Response Status:", response.status_code)
        # print("Response Text:", response.text)  # Print full error message from the backend
        assert response.status_code == 200, f"Unexpected status {response.status_code}: {response.text}"
        print(response.text)
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], str)

