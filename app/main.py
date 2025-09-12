from fastapi import FastAPI
from fastapi import HTTPException, Query
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "fastapi-service"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}

@app.get("/license")
def get_license(repo: str = Query(..., description="GitHub repository in the format 'owner/repo'")):
    """
    Retrieve the license information for a GitHub repository.
    """
    # parse and validate repo parameter
    parts = repo.split("/")
    if len(parts) != 2:
        raise HTTPException(status_code=400, detail="Invalid repo format. Use 'owner/repo'.")
    owner, name = parts
    url = f"https://api.github.com/repos/{owner}/{name}/license"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    if resp.status_code == 404:
        raise HTTPException(status_code=404, detail="Repository or license not found.")
    raise HTTPException(status_code=resp.status_code, detail=resp.text)
