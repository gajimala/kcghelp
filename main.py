from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="public", html=True), name="static")

@app.get("/lifesavers")
def get_lifesavers():
    with open("public/lifesavers.json", encoding="utf-8") as f:
        return json.load(f)
