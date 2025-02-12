# 15

## Overview
This script fetches award data from the USAspending API for a specified agency and extracts key details including recipient name, award type, award date, and total obligations in USD. In particular this is pulling from top tier Agency `015`. 

## Requirements
- Python 3.x
- `requests` library
- `pandas` library

## Installation
Ensure you have Python 3 installed and install the required dependencies:
```bash
pip install requests pandas
```

## Usage
Run the script using:
```bash
python3 15.py
```
When executed, the script will print a raw API response similar to the following:
```
Raw API Response: {'fiscal_year': 2025, 'latest_action_date': '2025-02-10T00:00:00', 'toptier_code': '015', 'transaction_count': 32317, 'obligations': 3247688297.8, 'messages': []}
```
This output changes depending on the latest available data from the API.

## Notes
- This script fetches real-time data from USASpending, so results will vary based on current data availability.
- Ensure you have an active internet connection when running the script.

