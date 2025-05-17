from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Dummy marks data (you can read from a file or database if needed)
marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40,
    "Eve": 50
}

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}
