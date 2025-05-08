from flask import Flask, Response
import pandas as pd
import httpx
from datetime import datetime
import json
from collections import OrderedDict
from dotenv import load_dotenv
import os


# Load environment variables from .env
load_dotenv()

# Planfix API details
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
API_PLANFIX_REPORT = os.getenv("API_PLANFIX_REPORT")


# Initialize Flask app
app = Flask(__name__)


# Get the ID of the latest saved report from the list of reports in Planfix
def get_latest_report_id():

    report_list_url = f"{API_PLANFIX_REPORT}/list"

    HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}"}

    response = httpx.post(report_list_url, headers=HEADERS)

    if response.status_code == 200:
        response_data = response.json()

        if response_data.get("result") == "success":
            reports = response_data.get("saves", [])

            if reports:
                max_id = max(report['id'] for report in reports)
                return max_id

            else:
                raise Exception("No reports found.")
        else:
            raise Exception(f"API Error: {response_data.get('errors')}")
    else:
        raise Exception(f"HTTP Error: {response.status_code} - {response.text}")


# API_1: Documentation in API_DOC.md at /planfix/fetch-report
# Fetches the data from the latest saved report from Planfix
@app.route("/fetch-report", methods=["GET"])
def fetch_report():

    # Get the latest report_id from the report`s list on Planfix
    report_id = get_latest_report_id()

    # Url to fetch report data from the latest report
    report_data_url = f"{API_PLANFIX_REPORT}/{report_id}/data"

    HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}"}

    response = httpx.post(report_data_url, headers=HEADERS)

    if response.status_code == 200:
        response_data = response.json()
        rows = response_data['data']['rows']

        # Extract header and rows
        header_row = next(row for row in rows if row['type'] == 'Header')
        headers = [item['text'] for item in header_row['items']]
        data_rows = [[item['text'] for item in row['items']] for row in rows if row['type'] == 'Normal']

        df = pd.DataFrame(data_rows, columns=headers)

        # Add new column with report_number
        report_number = f"report_{report_id}"
        df['Report_number'] = report_number
        df['Report_updated_at'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Convert DataFrame to JSON with ordered columns
        records = [OrderedDict(zip(df.columns, row)) for row in df.itertuples(index=False)]

        # Use json.dumps to serialize with explicit control
        json_data = json.dumps(records, ensure_ascii=False)

        return Response(json_data, content_type="application/json")

    else:
        return {"error": "Failed to fetch data"}, 500


if __name__ == '__main__':
    app.run(debug=True)
