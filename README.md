
# 📊 Power BI Report with Auto-Updated Data from Planfix via a Custom-Built API

The goal of this project is to build an automatically updating analytics dashboard in Power BI 
for monitoring the performance of a Marketing campaign using the data which is managed and 
continuously updated in `Planfix`.

The key challenge was integrating Power BI with the Planfix in a way that ensures:

- the report is always based on the most up-to-date data from Planfix
- the data is automatically retrieved and visualized without manual effort

To solve this, I developed a Flask-based API `Planfix Report API` and deployed it on a server to provide 
the most recent report data from Planfix in JSON format, which I used in Power BI 
as a data source.

## Project Goals:

✅ Automate data extraction and updates from Planfix

✅ Eliminate manual export/import

✅ Develop and support analytic report in Power BI

✅ Enable up-to-date analytics in Power BI

✅ Refresh the report multiple times per day to reflect real-time activity


## 🔄 Project Overview

- The Planfix Report API connects to Planfix and fetches the list of saved reports.
- It determines the latest report based on the highest ID.
- It retrieves the data of this latest report via a secure HTTP request, structured it into a pandas.DataFrame 
and returned as a JSON response.
- Power BI accesses data via Web connector (using API endpoint) and uses the JSON as a data source.
- Performed data cleaning and transformation, created the data model, calculated necessary metrics.
- Created necessary visualizations and comprehensive analytical report in Power BI Desktop.
- Managed the refresh policy in Power BI Service.


## Planfix Report API for Power BI Integration

This custom-built API Flask-based application provides an API that connects to the Planfix system and 
automatically fetches data from the latest saved report. 
It is used to power a real-time report in Power BI, ensuring that reporting is always based on 
the most up-to-date data from Planfix.

## Planfix Report API Overview

Planfix Report API was designed to automate the process of collecting structured data from Planfix and 
visualizing it in Power BI without manual export/import steps.

- Automated updates from Planfix
- Hosted on a server as a Flask web app
- Connected to Power BI via web API
- Used to build dashboards for monitoring and analysis

## Technologies Used

- Python 3.8+
- Flask
- httpx
- pandas
- dotenv
- Power BI – for dashboard visualization


## 🖥️ Deployment

This application is deployed on a remote server and exposed over HTTPS so that Power BI can access it as a web API. 
The endpoint is added to Power BI using Web connector.

## Power BI Integration

    In Power BI Desktop:

        Choose Get Data → Web.

        Enter the URL of the hosted API:
        https://your-server.com/fetch-report

    Load the data and use Power Query to transform it if needed.

    Build visuals based on the automatically refreshed report data.

## 📊 Power BI Report

Power BI report available here: [View the Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiMzk5MmIzZDMtOTFiNi00ZDg1LThmYTctMTU3ZDFiYmM4M2YxIiwidCI6ImIwYmYzYTRlLTBlMmMtNGQ5Ny1hMzUyLWY2MDY4MGFkYjZlMSIsImMiOjl9)

## 🔒 Data Privacy Notice

This report is provided for demonstration and viewing purposes only.
All sensitive or personal data has been anonymized to ensure compliance with privacy standards.

