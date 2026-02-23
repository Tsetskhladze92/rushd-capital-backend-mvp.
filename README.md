# Rushd Capital Backend MVP 

This is a professional Backend MVP developed with **FastAPI** for a Robo-advisor financial platform.

## Key Features

* **Modular Monolith  Architecture**: Organized into clean modules (auth, models, schemas).
* **Robust Security**:
  * OAuth2 with **JWT tokens** for secure session management.
  * Password hashing using **Bcrypt**.
* **Protected Endpoints**: Dynamic portfolio data access restricted to authorized users only.
* **Auto-documented API**: Fully functional Swagger UI (OpenAPI) integration.


## Tech Stack
* **Language**: Python 3.13
* **Framework**: FastAPI
* **ORM**: SQLAlchemy
* **Database**: SQLite (Development)

## Quick Start
1. Clone the repo: `git clone http://github.com/Tsetskhladze92/rushd-capital-backend-mvp.git`
2. Install dependencies `pip install -r requirements.txt`
3. Run the server: `uvicorn app.main:app --reload`
