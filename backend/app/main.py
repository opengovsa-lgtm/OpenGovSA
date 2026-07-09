from fastapi import FastAPI

app = FastAPI(title="OpenGovSA API", version="0.1.0")

@app.get("/")
def root():
    return {"application":"OpenGovSA","status":"online"}

@app.get("/health")
def health():
    return {"status":"healthy"}
