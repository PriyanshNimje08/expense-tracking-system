
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
* <img width="2560" height="1600" alt="image" src="https://github.com/user-attachments/assets/9054354b-9d1c-4d7e-bdba-e886cfb45b65" />

* SQL Database View
* <img width="1665" height="1222" alt="image" src="https://github.com/user-attachments/assets/c4772c70-2a86-4f75-929a-2974e1dc329f" />

* Server Log File
* <img width="2560" height="1600" alt="image" src="https://github.com/user-attachments/assets/ca310f94-ef28-46f9-92ef-d4e00a082e68" />

* Expense Analytics Charts
* <img width="2560" height="1600" alt="image" src="https://github.com/user-attachments/assets/8fe04726-ee6e-4d79-ba9b-8e2b37231481" />
<img width="2560" height="1600" alt="image" src="https://github.com/user-attachments/assets/c1e94a15-4ca7-4fe9-afda-942213dd3d4d" />
https://github.com/mehulcode12/codebasics_expense_tracking_with_sqlServer_FastAPI_Logging_Streamlit_pyDantic/blob/main/Screenshots/Screenshot%202025-04-04%20211306.png

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


