#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "data.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Creates the accounts table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            card_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            passcode_hash TEXT NOT NULL,
            balance INTEGER NOT NULL,
            phone_number TEXT UNIQUE NOT NULL,
            phone_charge INTEGER DEFAULT 0
        );
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def create_account(card_number, name, passcode_hash, balance, phone_number):
    """Adds a new account to the database."""
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO accounts (card_number, name, passcode_hash, balance, phone_number) VALUES (?, ?, ?, ?, ?)",
            (card_number, name, passcode_hash, balance, phone_number)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Card number or phone number already exists.")
        return False
    finally:
        conn.close()
    return True

def get_account(card_number):
    """Retrieves a single account by its card number."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE card_number = ?", (card_number,))
    account = cursor.fetchone()
    conn.close()
    return account

def update_balance(card_number, new_balance):
    """Updates the balance for a specific account."""
    conn = get_db_connection()
    conn.execute("UPDATE accounts SET balance = ? WHERE card_number = ?", (new_balance, card_number))
    conn.commit()
    conn.close()

initialize_database()
