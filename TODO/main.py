from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

class TodoBase(BaseModel):
    id: int
    task_body: str
    due_day: int
    due_month: str
    due_year: int

@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoBase, db: db_dependency):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    return {"detail": "Todo added successfully"}
