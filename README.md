
# Expense Management System

This project is an **Expense Management System** that consists of a **Streamlit frontend application**, **MySQL database**, and a **FastAPI backend server**.

This application allows users to manage their daily expenses, view analytics, and interact with a database for storing and retrieving expense data.

---

## Features

* Add or update daily expenses with details like amount, category, and notes.
* Analyze expenses over a date range with visualizations.
* Store expense data in a MySQL database.
* Backend powered by FastAPI for handling requests.
* Frontend built with Streamlit for a user-friendly experience.
* Secure authentication and user management.
* Export expenses as CSV or Excel for record-keeping.

---

## Tech Stack

* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit
* **Database:** MySQL
* **Other Libraries:** Pydantic, Requests

---

## Project Structure

```
Expense_Management_System/
├── backend/                           
│   ├── server.py                      # FastAPI server entry point
│   ├── server.log                     # Log file
│   ├── db_helper.py                   # Database helper functions for CRUD operations
│   ├── logging_setup.py               # Logging configuration for backend
│   └── tests/                         
│       ├── test_server.py             # Tests for FastAPI server
│       └── test_db_helper.py          # Tests for DB helper functions
│
├── frontend/                          
│   ├── app.py                         # Streamlit app entry point
│   ├── add_update_tab.py              # "Add/Update Expense" tab
│   ├── analytics_category.py          # "View Analytics by Category" tab
│   ├── analytics_month.py             # "View Analytics by Month" tab
│   ├── debugging.py                   # Debugging & integration code
│
├── database/                          
│   ├── init_db.sql                    # SQL script to initialize database
│   ├── db_config.py                   # Database connection configuration
│   └── migrations/                    
│       ├── 001_create_expenses_table.sql
│       └── 002_add_indexes.sql
│
├── tests/                             
│   ├── __init__.py                    
│   └── backend/                       
│       ├── test_db_helper.sql         # Tests DB helper functions
│
├── requirements.txt                   # Project dependencies
├── README.md                          # Project documentation
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the SQL server

* Open **SQL Workbench** (or any MySQL client).
* Import the SQL file from the `database/` directory.
* Update your **host, user, and password** in `db_config.py`.

### 4. Run the FastAPI server

```bash
uvicorn backend.server:app --reload
```

### 5. Run the Streamlit app

(Use a second terminal)

```bash
streamlit run frontend/app.py
```

---

## API Endpoints

* **GET** `/expenses/{expense_date}` → Fetch expenses for a specific date.
* **PUT** `/expenses/{expense_date}` → Update expenses for a specific date.
* **POST** `/analytics/` → Fetch expense summary for a date range.
* **POST** `/export/` → Export expense data as CSV or Excel.

---

## Screenshots & Recordings

(Add your screenshots & screen recordings here after uploading them to a public location)

* Adding/Updating Expenses
* SQL Database View
* Server Log File
* Expense Analytics Charts

---

## License

This project is licensed under the **MIT License** – see the LICENSE file for details.

---

## Contributing

Contributions are welcome! 🚀

**Need of Contributor:**

* Secure authentication and user management.
* Export expenses as CSV or Excel.

### Steps to Contribute

1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes with clear messages
4. Push the branch and create a Pull Request

For major changes, open an issue first to discuss proposed modifications.

---

क्या आप चाहोगे कि मैं इसमें **badges (Python, FastAPI, Streamlit, MySQL, MIT License)** भी डाल दूँ ताकि README और professional लगे?
