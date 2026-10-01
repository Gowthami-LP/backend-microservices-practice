import requests
from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(title="User Service")

# Basic endpoint to check whether Service 1 is running
@app.get("/")
def home():
    return {
        "service": "User Service",
        "status": "running"
    }

# Health-check endpoint
@app.get("/health")
def health():
    return {
        "service": "User Service",
        "status": "healthy"
    }

# Return sample user information
@app.get("/users/1")
def get_user():
    return {
        "user_id": 1,
        "name": "Gowthami",
        "email": "gowthami@example.com"
    }

# Service 1 calls Service 2
@app.get("/call-order-service")
def call_order_service():

    # URL of Service 2
    order_service_url = "http://127.0.0.1:8002/orders/1001"

    # Send HTTP GET request to Service 2
    response = requests.get(order_service_url)

    # Convert Service 2 response into JSON
    order_data = response.json()

    # Return Service 2 response
    return {
        "message": "Successfully called Order Service",
        "order_service_response": order_data
    }
