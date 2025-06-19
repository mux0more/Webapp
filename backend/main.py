from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Evaluation(BaseModel):
    userId: int
    ratings: Dict[str, int]

def get_db_connection():
    conn = sqlite3.connect('evaluations.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
async def startup():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS student_evaluations
                 (user_id INTEGER, criterion TEXT, rating INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS teacher_evaluations
                 (user_id INTEGER, criterion TEXT, rating INTEGER)''')
    conn.commit()
    conn.close()

@app.post("/evaluate/student")
async def evaluate_student(evaluation: Evaluation):
    conn = get_db_connection()
    c = conn.cursor()
    for criterion, rating in evaluation.ratings.items():
        c.execute("INSERT INTO student_evaluations (user_id, criterion, rating) VALUES (?, ?, ?)",
                  (evaluation.userId, criterion, rating))
    conn.commit()
    conn.close()
    return {"message": "Оценка сохранена"}

@app.post("/evaluate/teacher")
async def evaluate_teacher(evaluation: Evaluation):
    conn = get_db_connection()
    c = conn.cursor()
    for criterion, rating in evaluation.ratings.items():
        c.execute("INSERT INTO teacher_evaluations (user_id, criterion, rating) VALUES (?, ?, ?)",
                  (evaluation.userId, criterion, rating))
    conn.commit()
    conn.close()
    return {"message": "Оценка сохранена"}