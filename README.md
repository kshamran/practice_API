  Telusko Trac — Inventory & Product Management System

Telusko Trac is a lightweight inventory and product management system built with **FastAPI (Python)** for the backend and **React** for the frontend.  
It’s designed to help businesses manage their products, track inventory, and perform CRUD operations efficiently — all through a clean and modern interface.

---

 Tech Stack

Frontend
- React
- Axios for API communication
- Tailwind CSS for styling
- React Router for page navigation

**Backend**
- FastAPI
- SQLAlchemy ORM
- PostgreSQL / SQLite (configurable)
- Pydantic for data validation
- CORS Middleware for frontend-backend communication

---

 Project Structure

telusko-trac/
│
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── database.py # Database connection and session setup
│ ├── database_models.py # SQLAlchemy models
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ ├── src/
│ │ ├── App.js # Main React logic
│ │ ├── index.js # React entry point
│ │ ├── components/ # Reusable UI components
│ │ └── pages/ # Page-level components
│ ├── package.json # Frontend dependencies
│ └── public/ # Static assets
│
└── README.md


  Setup Instructions

 1️. Clone the Repository
```bash
git clone https://github.com/your-username/telusko-trac.git
cd telusko-trac

2️. Backend Setup (FastAPI)
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


✅ The backend will run at
http://127.0.0.1:8000

3.  Frontend Setup (React)
cd ../frontend
npm install
npm start


 The frontend will run at
http://localhost:3000

 API Endpoints
Method	Endpoint	Description
GET	/products/	Retrieve all products
POST	/products/	Add a new product
GET	/products/{id}	Get product by ID
PUT	/products/{id}	Update product
DELETE	/products/{id}	Delete product
 Features

Add, update, and delete products

Real-time product list with sorting and filtering

Responsive interface

CORS-enabled communication between frontend and backend

Editable form system with instant feedback messages

 Author

Shamran
Built with  using FastAPI & React.
