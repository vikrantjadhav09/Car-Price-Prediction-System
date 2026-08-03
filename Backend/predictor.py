from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "car_price_prediction_pipeline.joblib"

model = joblib.load(MODEL_PATH)


def predict_price(car):
    df = pd.DataFrame([car])

    prediction = model.predict(df)

    return int(prediction[0])