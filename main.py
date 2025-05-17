from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Read JSON file at import time
json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(json_path, "r") as f:
    data = json.load(f)

# Create a name → marks dictionary
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [marks_dict.get(n) for n in name]
    return {"marks": result}
