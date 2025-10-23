from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import database_models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or specify your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
    
)


# Create the database tables
database_models.Base.metadata.create_all(bind=engine)

# ----------------- SCHEMAS -----------------
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

    class Config:
        from_attributes = True


# ----------------- DB SESSION -----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------- INITIAL DATA -----------------
def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count()
    if count == 0:
        products = [
            {"name": "Laptop", "description": "A good laptop", "price": 50000.0, "quantity": 15},
            {"name": "Phone", "description": "A good phone", "price": 30000.0, "quantity": 10},
            {"name": "Tablet", "description": "A good tablet", "price": 35000.0, "quantity": 6},
        ]
        for p in products:
            db.add(database_models.Product(**p))
        db.commit()
    db.close()


@app.on_event("startup")
def startup():
    init_db()


# ----------------- ROUTES -----------------
@app.get("/")
def read_root():
    return {"message": "Hello Shamran, just go and code my bro!!!!"}


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        return product
    return {"error": "Product not found"}


@app.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"message": "Product added successfully", "product": db_product}


@app.patch("/products/{id}")
def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        return {"error": "Product not found"}
    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully", "product": db_product}
