import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "fintrack.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS transactions (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       type TEXT NOT NULL,
                       category TEXT NOT NULL,
                       amount REAL NOT NULL,
                       description TEXT,
                       date TEXT NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()
def add_transaction(type, category, amount, description, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO transactions(type, category, amount, description, date)
                   VALUES(?,?,?,?,?)""",(type, category, amount, description, date)
    )
    conn.commit()
    conn.close()
def get_transactions():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM transactions ORDER BY date DESC", conn)
    conn.close()
    return df 
def delete_transaction(transaction_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
def get_summary():
    df = get_transactions()
    if df.empty:
        return {"income": 0,"expenses":0,"balance":0}
    income = df[df["type"]=="income"]["amount"].sum()
    expenses = df[df["type"]=="expense"]["amount"].sum()
    balance = income - expenses 
    return {
        "income":round(income, 2),
        "expenses":round(expenses, 2),
        "balance":round(balance, 2)
    }
    