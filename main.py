from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# PASTE YOUR JSON DATA HERE directly
marks_list = [
    {"name": "mGHfxNF", "marks": 80},
    {"name": "5tG", "marks": 67},
    {"name": "n", "marks": 60},
    {"name": "7pdBs9CA", "marks": 55},
    {"name": "3YUhWw", "marks": 42},
    {"name": "Wyx2lKN8", "marks": 62},
    {"name": "xYpiUkMRyI", "marks": 42}
]

# Build dict for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: List[str] = []):
    return {"marks": [marks_dict.get(n) for n in name]}
