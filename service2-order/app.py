import requests
from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(title="Order Service")

# Basic endpoint
@app.get("/")
def home():
    return {
        "service": "Order Service",
        "status": "running"
    }

# Health-check endpoint
@app.get("/health")
def health():
    return {
        "service": "Order Service",
        "status": "healthy"
    }

# Return sample order information
@app.get("/orders/1001")
def get_order():
    return {
        "order_id": 1001,
        "user_id": 1,
        "product": "Laptop",
        "quantity": 1
    }

# Service 2 calls Service 3
@app.get("/call-notification-service")
def call_notification_service():

    # URL of Service 3
    notification_url = "http://127.0.0.1:8003/notify/1"

    # Call Service 3
    response = requests.get(notification_url)

    # Convert response into JSON
    notification_data = response.json()

    return {
        "message": "Successfully called Notification Service",
        "notification_response": notification_data
    }
