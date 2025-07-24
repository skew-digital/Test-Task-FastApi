from fastapi import FastAPI, HTTPException
from app.services.processor import process_message
from app.models.schemas import CustomerMessage, CustomerResponse

app = FastAPI()


@app.post(
    "/process-customer-message",
    response_model=CustomerResponse,
    tags=["Customer Message Processing"],
)
def process_customer_message(payload: CustomerMessage):
    try:
        # process the message
        response = process_message(payload.message)

        # return the response
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
