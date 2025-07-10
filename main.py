from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import uvicorn

from src.database import SessionLocal
from src.models.automobile import Automobile

app = FastAPI(title="Automobile Search API", version="1.0.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency para obter sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos Pydantic para request/response
class AutomobileFilter(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    color: Optional[str] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    mileage_max: Optional[int] = None

class AutomobileResponse(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str
    mileage: int
    price: float
    fuel_type: str
    transmission: str
    engine_size: float
    num_doors: int
    plate: str

    class Config:
        from_attributes = True

@app.get("/")
def read_root():
    return {"message": "Automobile Search API - MCP Protocol"}

@app.post("/search", response_model=List[AutomobileResponse])
def search_automobiles(filters: AutomobileFilter, db: Session = Depends(get_db)):
    """
    Buscar automóveis com base nos filtros fornecidos.
    Implementa o protocolo MCP (Model Communication Protocol).
    """
    query = db.query(Automobile)
    
    # Aplicar filtros
    if filters.brand:
        query = query.filter(Automobile.brand.ilike(f"%{filters.brand}%"))
    
    if filters.model:
        query = query.filter(Automobile.model.ilike(f"%{filters.model}%"))
    
    if filters.year_min:
        query = query.filter(Automobile.year >= filters.year_min)
    
    if filters.year_max:
        query = query.filter(Automobile.year <= filters.year_max)
    
    if filters.color:
        query = query.filter(Automobile.color.ilike(f"%{filters.color}%"))
    
    if filters.price_min:
        query = query.filter(Automobile.price >= filters.price_min)
    
    if filters.price_max:
        query = query.filter(Automobile.price <= filters.price_max)
    
    if filters.fuel_type:
        query = query.filter(Automobile.fuel_type.ilike(f"%{filters.fuel_type}%"))
    
    if filters.transmission:
        query = query.filter(Automobile.transmission.ilike(f"%{filters.transmission}%"))
    
    if filters.mileage_max:
        query = query.filter(Automobile.mileage <= filters.mileage_max)
    
    automobiles = query.all()
    return automobiles

@app.get("/automobiles", response_model=List[AutomobileResponse])
def get_all_automobiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obter todos os automóveis com paginação.
    """
    automobiles = db.query(Automobile).offset(skip).limit(limit).all()
    return automobiles

@app.get("/automobiles/{automobile_id}", response_model=AutomobileResponse)
def get_automobile(automobile_id: int, db: Session = Depends(get_db)):
    """
    Obter um automóvel específico por ID.
    """
    automobile = db.query(Automobile).filter(Automobile.id == automobile_id).first()
    if automobile is None:
        raise HTTPException(status_code=404, detail="Automóvel não encontrado")
    return automobile

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

