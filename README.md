# FinTrack — Personal Finance Tracker

A clean, interactive personal finance dashboard built with Python and Streamlit.
Track your income and expenses, visualize spending patterns, and monitor monthly trends.

## Features
- Add and categorize income and expense transactions
- Real-time balance, total income and total expense metrics
- Spending breakdown by category (donut chart)
- Income vs expenses comparison (bar chart)
- Monthly trends tracking (line chart)
- Full transaction history with delete functionality
- Data persisted locally using SQLite

## Tech Stack
- **Streamlit** — web dashboard UI
- **Pandas** — data processing and analysis
- **Plotly** — interactive charts
- **SQLite** — local database storage

## Project Structure
FinTrack/
├── app.py                  → main Streamlit dashboard
├── requirements.txt        → dependencies
└── utils/
    ├── database.py         → SQLite CRUD operations
    └── charts.py           → Plotly chart generation

## How to Run

1. Clone the repository
   git clone https://github.com/itzPR4TIK/FinTrack.git

2. Install dependencies
   pip install -r requirements.txt

3. Start the app
   streamlit run app.py

4. Open browser at http://localhost:8501

## Author
Pratik Nagpure — github.com/itzPR4TIK