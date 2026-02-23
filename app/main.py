from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, database, utils

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = utils.hash_password(user.password)

    new_user = models.User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=403, detail="Incorrect data.")
    
    if not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect data.")
    
    access_token = utils.create_access_token(data={"user_id": user.id})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
        }

@app.get("/my-portfolio")
def get_portfolio(token: str = Depends(oauth2_scheme)):

    return {
        "status": "Success",
        "message": "Welcome to your Rushd Capital portfolio!",
        "data": {
            "balance": "15,000 USD",
            "assets": ["Gold", "Ethical Stocks", "Real Estate"]
        }
    }