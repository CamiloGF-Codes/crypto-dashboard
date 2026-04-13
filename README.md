# Crypto Dashboard

REST API that ingests real-time cryptocurrency data from CoinGecko, 
stores historical prices in PostgreSQL, and visualizes trends through 
a custom web dashboard.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** HTML, Bootstrap 5, Chart.js
- **Deploy:** Railway (backend), Netlify (frontend)

## Project Structure

\```
crypto-dashboard/
├── backend/
│   ├── app/
│   │   ├── routes/       # API endpoints
│   │   ├── services/     # Business logic
│   │   ├── repositories/ # Database layer
│   │   └── models/       # SQLAlchemy models
│   ├── tests/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html
│   └── app.js
└── README.md
\```

## Setup

\```bash
# 1. Clone the repo
git clone https://github.com/CamiloGF-Codes/crypto-dashboard.git
cd crypto-dashboard/backend

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your values

# 5. Run the API
uvicorn main:app --reload
\```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API status |
| GET | `/health` | Health check |

## Author

Camilo González — [GitHub](https://github.com/CamiloGF-Codes)

## Live Demo

- **API:** https://crypto-dashboard-rvy9.onrender.com
- **Dashboard:** https://cryptos-dashboard13.netlify.app
- **API Docs:** https://crypto-dashboard-rvy9.onrender.com/docs