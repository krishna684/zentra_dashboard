import os

import requests
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv()

# Use the repository root as the template folder so Netlify can serve
# the same index.html file that Flask renders.
app = Flask(__name__, template_folder='.')

API_TOKEN = os.getenv('ZENTRA_API_TOKEN')
# Comma-separated list of device IDs
DEVICE_IDS = [d.strip() for d in os.getenv('ZENTRA_DEVICE_IDS', '').split(',') if d.strip()]

def fetch_device_data(device_id: str, start: str | None = None, end: str | None = None):
    """Fetch data from the ZENTRA Cloud API for a single device."""
    if not API_TOKEN:
        return None

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    url = f"https://api.zentracloud.com/v1/devices/{device_id}/data"
    params = {}
    if start:
        params["start"] = start
    if end:
        params["end"] = end
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None


@app.route('/')
def index():
    return render_template('index.html', device_ids=DEVICE_IDS)

@app.route('/data/<device_id>')
def get_data(device_id):
    """Return JSON data for a device given optional start/end params."""
    start = request.args.get('start')
    end = request.args.get('end')
    data = fetch_device_data(device_id, start=start, end=end)
    if data is not None:
        return jsonify(data)
    return jsonify({'error': 'Failed to fetch data'}), 500


@app.route('/sensors')
def list_sensors():
    """Return available sensor/device IDs."""
    return jsonify({'devices': DEVICE_IDS})

if __name__ == '__main__':
    app.run(debug=True)
