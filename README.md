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
When executed, the script will print a raw API response similar to the following, and you should see: 

<img width="707" alt="Screenshot 2025-02-12 at 10 42 56 PM" src="https://github.com/user-attachments/assets/863274aa-d3b1-4753-bec1-310b66087459" />

This output changes depending on the latest available data from the API.

## Notes
- This script fetches real-time data from USASpending, so results will vary based on current data availability.
- Ensure you have an active internet connection when running the script.

