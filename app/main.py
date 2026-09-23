from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello from Release Manager Demo - Version 2",
        "environment": "DEV",
        "version": "2.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "2.0"
    }