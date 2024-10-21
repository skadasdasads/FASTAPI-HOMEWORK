from fastapi import FastaAPI, Depends
from database import session_local, engine
import models, schemas, teacher_crud
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind = engine)

app = FastAPI()


def get_db():
    db = session_local() 
    try : 
        yield db
    finally: 
        db.close() 
        
        
@app.post("/calculate", response_model=schemas.CalculationResponse)
async def calculate(calculation: schemas.CalculationCreate,
                    db: Session = Depends(get_db)):
    
    reponse = calculate.crud.create_calculation(db, calculation) 
    
    return response


@app.get("/calculate", response_model=list[schemas.CalculationResponse])
async def find_all_calculation(db: Session = Depends(get_db)):
    
    all_calculation = calculate.get_all_calculation(db)
    
    return all_calculation


@app.get("/calculate/{calculate_id}",response_model=schemas.CalculationResponse])
async def find_calculation_by_id(calculation_id:int, db: Session = Depends(get_db)):
    
    db_calculation = calculation_crud.get_calculation_by_id(db, calculation_id)
    
    return db_calculation