CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,       
    amount REAL NOT NULL,
    category TEXT,
    date DATETIME NOT NULL
);