from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(title="Notification Service")

# Basic endpoint
@app.get("/")
def home():
    return {
        "service": "Notification Service",
        "status": "running"
    }

# Health-check endpoint
@app.get("/health")
def health():
    return {
        "service": "Notification Service",
        "status": "healthy"
    }

# Notification endpoint
@app.get("/notify/{user_id}")
def notify_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "Notification sent successfully"
    }
