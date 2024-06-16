from typing import List, Optional
#
from fastapi import FastAPI, Response, APIRouter, Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session
#
from .. import models, schemas
from ..database import get_db

# Organizes and modularizes the application, grouping related routes in a single location
router = APIRouter(
    prefix="/menu",
    tags=['Order']
)

# [GET] Requests The Restaurant Menu Through Categories
@router.get("/categories", response_model=List[schemas.MenuResponse])
def get_by_categories(db: Session = Depends(get_db),
             search: Optional[str]=""):
    
    query = (db.query(models.Product)
            .filter(models.Product.category == search))
    
    products = query.all()
    
    return products

# [GET] Requests The Restaurant Menu Through Name/Description
@router.get("/product", response_model=List[schemas.MenuResponse])
def get_by_name_descrip(db: Session = Depends(get_db),
                search: Optional[str]=""):
    
    query = (db.query(models.Product)
                .filter(
                    or_(
                        models.Product.name.ilike(f"%{search}%"),
                        models.Product.description.ilike(f"%{search}%")
                    )
                )
            )
    
    products = query.all()
    
    return products

# [GET] Requests The Restaurant Menu Through isOnOffer Column
@router.get("/on-offer", response_model=List[schemas.MenuResponse])
def get_products_on_offer(db: Session = Depends(get_db)):
    
    query = (db.query(models.Product)
                .filter(
                    models.Product.isOnOffer == True
                )
            )

    products = query.all()
    
    return products
