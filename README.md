# Azure-Simulate-Guardian
> Azure cost simulation tool with Flask and SQLite backend.

![Python](https://img.shields.io/badge/python-3.10+-blue) ![Flask](https://img.shields.io/badge/flask-2.x-lightgrey) ![Azure](https://img.shields.io/badge/azure-simulation-0078D4)

## What it does
Simulates Azure infrastructure behavior and models resource governance.
Translates cloud architecture configs into cost calculation logic.
Outputs results via a web dashboard backed by SQLite.

## Tech Stack
- Python, Flask, SQLite, HTML

## Quick Start
```bash
git clone https://github.com/Husseinuahmedc/Azure-Simulate-Guardian
cd Azure-Simulate-Guardian
pip install -r requirements.txt
python app.py
```

## Architecture
```
User Input → Flask App → Simulation Logic → SQLite DB
                                         ↓
                                  Cost Calculation
                                         ↓
                                  Output Dashboard
```

## Notes
No real Azure subscription needed. All simulation runs locally.
