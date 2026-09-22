from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello from Release Manager Demo",
        "environment": "DEV"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }