from fastapi import FastAPI
from Backend.schemas import CarFeatures
from Backend.predictor import predict_price
from fastapi import HTTPException


app = FastAPI(
    title="Car Price Prediction API"
)


@app.get("/")
def home():
    return {"message": "API Running 🚗"}


from fastapi import HTTPException

@app.post("/predict")
def predict(car: CarFeatures):
    try:
        prediction = predict_price(car.model_dump())

        return {
            "success": True,
            "predicted_price": int(prediction),
            "currency": "INR",
            "message": "Prediction Successful"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))