from fastapi import FastAPI 


app = FastAPI() 

@app.get("/shipment")
def get_shippment(): 
    return {
        "content": "Asus Laptop", 
        "status": "in transit"

    }