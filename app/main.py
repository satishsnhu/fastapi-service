from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "fastapi-service"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}

@app.get("/greet")
def greet(name: str = "world"):
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    return {"message": f"{greeting}, {name}!"}