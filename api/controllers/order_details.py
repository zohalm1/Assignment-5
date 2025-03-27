# controllers/order_details.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.OrderDetail, tags=["Order Details"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return crud.create_order_detail(db=db, order_detail=order_detail)

@router.get("/", response_model=List[schemas.OrderDetail], tags=["Order Details"])
def read_order_details(db: Session = Depends(get_db)):
    return crud.get_order_details(db=db)

@router.get("/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def read_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = crud.get_order_detail(db=db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_detail

@router.put("/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def update_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    updated_order_detail = crud.update_order_detail(db=db, order_detail_id=order_detail_id, order_detail=order_detail)
    if updated_order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return updated_order_detail

@router.delete("/{order_detail_id}", tags=["Order Details"])
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = crud.delete_order_detail(db=db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return {"detail": "Order Detail deleted successfully"}
