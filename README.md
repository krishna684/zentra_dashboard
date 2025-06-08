# ZENTRA Dashboard

A Flask web dashboard that fetches real-time and historical environmental sensor data from the ZENTRA Cloud API and visualises it using Chart.js.

## Features
- Supports multiple sensors configured via the `ZENTRA_DEVICE_IDS` environment variable.
- Fetch historical data by specifying start and end date ranges.
- Chart.js line charts display the measurements.
- API tokens and device IDs are read from a `.env` file (see `.env.example`).
- Foundation for future extensions such as alerts and integration with time-series databases or cloud services.

## Setup
1. Create a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask requests python-dotenv
   ```
2. Copy `.env.example` to `.env` and fill in your ZENTRA Cloud API token and device IDs.
3. Start the Flask development server:
   ```bash
   python app.py
   ```
4. Visit `http://localhost:5000` in your browser.

If deploying to a static host such as Netlify, serve the `index.html` file from the project root so the dashboard loads correctly.

## Extending
The code is organised so `fetch_device_data` can be reused by background jobs or integrations. Future enhancements might store data in a time-series database or trigger alerts when measurements exceed thresholds.
