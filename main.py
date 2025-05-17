from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get path to JSON file relative to current file
json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

# Read JSON once at startup
with open(json_path, "r") as f:
    marks_list = json.load(f)

# Build dict for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
async def get_marks(request: Request):
    query_params = request.query_params.getlist("name")
    result = [marks_dict.get(name) for name in query_params]
    return JSONResponse(content={"marks": result})
