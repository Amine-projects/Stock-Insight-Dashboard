#  Stock Insight Dashboard

A powerful, modular dashboard application for analyzing stock market data using technical indicators and custom visualizations. Built with FastAPI and designed for extensibility and performance.

---

##  Features

-  Visualize stock data with interactive charts
-  Compute and display technical indicators
-  Modular architecture for utilities, models, and API interaction
-  FastAPI backend for high-performance async APIs
-  Unit and integration tests included
-  Caching support for efficient data handling

---

## Project Structure

stock-insight-dashboard/
├── app/
│ ├── core/ # Configuration and security logic
│ ├── models/ # Pydantic schemas and response models
│ ├── utils/ # Technical indicators, API clients, plot utilities
│ ├── tests/ # Unit and integration tests
│ └── main.py # FastAPI application entry point
├── .env # Environment configuration file
├── .gitignore # Git ignore rules
├── requirements.txt # Project dependencies
├── requirements-dev.txt # Dev tools for linting and testing
└── README.md # Project documentation


## 📦 Installation

### Prerequisites

- Python 3.10+
- `pip` (or `poetry`, optionally)

### 1. Clone the repository

```
git clone https://github.com/yourusername/stock-insight-dashboard.git
cd stock-insight-dashboard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy or create a .env file in the root directory and set any required keys (e.g., API keys, secrets).

## Running the App

### Start the FastAPI server

```
uvicorn app.main:app --reload
```

### 🧪 Running Tests

Make sure dev dependencies are installed:
```
pip install -r requirements-dev.txt
```

Then run:

```
pytest
```
