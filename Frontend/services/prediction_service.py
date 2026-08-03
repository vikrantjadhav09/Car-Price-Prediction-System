"""
=========================================================
Prediction Service
AI Powered Car Price Prediction System
---------------------------------------------------------
Business logic for predictions.
=========================================================
"""

from __future__ import annotations

from typing import Dict, Any

from services.api import api


class PredictionService:
    """
    Business logic for prediction.
    """

    REQUIRED_FIELDS = [
        "company",
        "model",
        "year",
        "fuel_type",
        "kms_driven",
    ]

    # =====================================================
    # VALIDATION
    # =====================================================

    @staticmethod
    def validate(data: Dict[str, Any]) -> tuple[bool, str]:

        if not isinstance(data, dict):
            return False, "Invalid request."

        for field in PredictionService.REQUIRED_FIELDS:

            if field not in data:
                return False, f"{field} is required."

            if data[field] in ("", None):
                return False, f"{field} cannot be empty."

        if int(data["year"]) < 1990:
            return False, "Invalid manufacturing year."

        if int(data["kms_driven"]) < 0:
            return False, "Kilometers cannot be negative."

        return True, ""

    # =====================================================
    # FORMAT PAYLOAD
    # =====================================================

    @staticmethod
    def prepare_payload(data: Dict[str, Any]):

        return {
            "company": data["company"],
            "model": data["model"],
            "year": int(data["year"]),
            "fuel_type": data["fuel_type"],
            "kms_driven": int(data["kms_driven"]),
        }

    # =====================================================
    # PREDICT
    # =====================================================

    @staticmethod
    def predict(data: Dict[str, Any]) -> Dict[str, Any]:

        valid, message = PredictionService.validate(data)

        if not valid:
            return {
                "success": False,
                "message": message,
            }

        payload = PredictionService.prepare_payload(data)

        return api.predict(payload)

    # =====================================================
    # FORMAT PRICE
    # =====================================================

    @staticmethod
    def format_price(price):

        try:
            return f"₹ {float(price):,.0f}"

        except Exception:
            return "₹ 0"

    # =====================================================
    # CONFIDENCE
    # =====================================================

    @staticmethod
    def confidence(score=None):

        if score is None:
            return 95

        try:
            return round(float(score), 2)
        except Exception:
            return 95

    # =====================================================
    # RESULT SUMMARY
    # =====================================================

    @staticmethod
    def summary(result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert FastAPI response into a frontend-friendly format.
        """

        if not result.get("success", False):
            return {
                "success": False,
                "message": result.get("message", "Prediction failed.")
            }

        return {
            "success": True,
            "price": PredictionService.format_price(
                result.get("predicted_price", 0)
            ),
            "confidence": PredictionService.confidence(
                result.get("confidence", 95)
            ),
            "currency": result.get("currency", "INR"),
            "message": result.get("message", "Prediction Successful")
        }

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    @staticmethod
    def backend_online():

        return api.ping()


prediction_service = PredictionService()