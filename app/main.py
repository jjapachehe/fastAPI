from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {
        "content": "Wooden table",
        "status": "in transit"
    }