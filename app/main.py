from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "fastapi-service"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}

