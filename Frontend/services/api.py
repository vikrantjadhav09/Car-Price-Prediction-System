"""
=========================================================
API Service Layer
AI Powered Car Price Prediction System
---------------------------------------------------------
Handles all communication between Streamlit and FastAPI.
=========================================================
"""

from __future__ import annotations

import logging
from typing import Any

import requests

# =========================================================
# CONFIGURATION
# =========================================================

API_HOST = "127.0.0.1"
API_PORT = 8000

BASE_URL = f"http://{API_HOST}:{API_PORT}"

TIMEOUT = 30


# =========================================================
# LOGGER
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# =========================================================
# API CLIENT
# =========================================================

class APIClient:
    """
    Reusable API Client
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout: int = TIMEOUT,
    ):

        self.base_url = base_url.rstrip("/")

        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    # =====================================================
    # URL
    # =====================================================

    def url(self, endpoint: str):

        endpoint = endpoint.lstrip("/")

        return f"{self.base_url}/{endpoint}"

    # =====================================================
    # GET
    # =====================================================

    def get(
        self,
        endpoint: str,
        params: dict | None = None,
    ) -> dict:

        try:

            response = self.session.get(
                self.url(endpoint),
                params=params,
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(e)

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # POST
    # =====================================================

    def post(
        self,
        endpoint: str,
        payload: dict,
    ) -> dict:

        try:

            response = self.session.post(
                self.url(endpoint),
                json=payload,
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(e)

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    def health(self):

        return self.get("/health")

    # =====================================================
    # MODEL INFO
    # =====================================================

    def model_info(self):

        return self.get("/model/info")

    # =====================================================
    # VERSION
    # =====================================================

    def version(self):

        return self.get("/version")

    # =====================================================
    # ROOT
    # =====================================================

    def root(self):

        return self.get("/")

    # =====================================================
    # PREDICT
    # =====================================================

    def predict(self, features: dict) -> dict:
        """
        Predict car price.

        Example:
        {
            "company": "Hyundai",
            "model": "i20",
            "year": 2019,
            "fuel_type": "Petrol",
            "kms_driven": 45000
        }
        """

        return self.post(
            "/predict",
            features
        )

    # =====================================================
    # BATCH PREDICTION
    # =====================================================

    def batch_predict(
        self,
        records: list[dict],
    ) -> dict:
        """
        Predict multiple cars.
        """

        payload = {
            "records": records
        }

        return self.post(
            "/predict/batch",
            payload
        )

    # =====================================================
    # DATASET INFORMATION
    # =====================================================

    def dataset_info(self) -> dict:
        """
        Dataset statistics.
        """

        return self.get(
            "/dataset/info"
        )

    # =====================================================
    # DATASET SAMPLE
    # =====================================================

    def dataset_sample(
        self,
        rows: int = 10,
    ) -> dict:
        """
        Sample rows from dataset.
        """

        return self.get(
            "/dataset/sample",
            {
                "rows": rows
            }
        )

    # =====================================================
    # AVAILABLE BRANDS
    # =====================================================

    def companies(self):
        """
        Get available companies.
        """

        return self.get(
            "/companies"
        )

    # =====================================================
    # CAR MODELS
    # =====================================================

    def models(
        self,
        company: str,
    ):
        """
        Get models for a company.
        """

        return self.get(
            "/models",
            {
                "company": company
            }
        )

    # =====================================================
    # FUEL TYPES
    # =====================================================

    def fuel_types(self):
        """
        Available fuel types.
        """

        return self.get(
            "/fuel-types"
        )

    # =====================================================
    # YEARS
    # =====================================================

    def years(self):
        """
        Manufacturing years.
        """

        return self.get(
            "/years"
        )

    # =====================================================
    # PREDICTION HISTORY
    # =====================================================

    def prediction_history(
        self,
        limit: int = 100,
    ):
        """
        Prediction history.
        """

        return self.get(
            "/history",
            {
                "limit": limit
            }
        )

    # =====================================================
    # SINGLE HISTORY RECORD
    # =====================================================

    def history_by_id(
        self,
        prediction_id: int,
    ):
        """
        Get one prediction.
        """

        return self.get(
            f"/history/{prediction_id}"
        )

    # =====================================================
    # DELETE HISTORY
    # =====================================================

    def delete_prediction(
        self,
        prediction_id: int,
    ):
        """
        Delete one prediction.
        """

        try:

            response = self.session.delete(
                self.url(
                    f"/history/{prediction_id}"
                ),
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(e)

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # CLEAR HISTORY
    # =====================================================

    def clear_history(self):
        """
        Delete all predictions.
        """

        try:

            response = self.session.delete(
                self.url("/history"),
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(e)

            return {

                "success": False,

                "message": str(e)

            }

    # =====================================================
    # API PING
    # =====================================================

    def ping(self):
        """
        Quick connectivity check.
        """

        try:

            response = self.session.get(
                self.url("/"),
                timeout=5,
            )

            return response.status_code == 200

        except Exception:

            return False


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================

class APIError(Exception):
    """Base API exception."""
    pass


class ConnectionError(APIError):
    """Connection failed."""
    pass


class PredictionError(APIError):
    """Prediction failed."""
    pass


# =========================================================
# RESPONSE HELPERS
# =========================================================

def is_success(response: dict) -> bool:
    """
    Returns True if API call succeeded.
    """

    if not isinstance(response, dict):
        return False

    return response.get("success", False)


def get_message(response: dict) -> str:
    """
    Extract response message.
    """

    if not isinstance(response, dict):
        return "Invalid response."

    return response.get("message", "")


def get_data(response: dict):
    """
    Extract response data.
    """

    if not isinstance(response, dict):
        return None

    return response.get("data")


# =========================================================
# HEALTH CHECK
# =========================================================

def is_backend_online() -> bool:
    """
    Check backend availability.
    """

    try:

        return api.ping()

    except Exception:

        return False


# =========================================================
# UPDATE CONFIGURATION
# =========================================================

def set_base_url(
    host: str,
    port: int,
):
    """
    Update API host dynamically.
    """

    global api

    api = APIClient(
        base_url=f"http://{host}:{port}"
    )

    logger.info(
        f"API Base URL updated → {api.base_url}"
    )


# =========================================================
# API INFORMATION
# =========================================================

def api_information():
    """
    Basic client information.
    """

    return {

        "base_url": api.base_url,

        "timeout": api.timeout,

        "headers": dict(api.session.headers)

    }


# =========================================================
# CLOSE SESSION
# =========================================================

def close():
    """
    Close HTTP session.
    """

    try:

        api.session.close()

        logger.info(
            "HTTP session closed."
        )

    except Exception as e:

        logger.error(e)


# =========================================================
# SINGLETON INSTANCE
# =========================================================

api = APIClient()


# =========================================================
# SELF TEST
# =========================================================

if __name__ == "__main__":

    print("=" * 60)

    print("AI Powered Car Price Prediction")

    print("=" * 60)

    print()

    print("Backend Online : ", api.ping())

    print("Health : ")

    print(api.health())

    print()

    print("Version : ")

    print(api.version())

    print()

    print("Model Info : ")

    print(api.model_info())

    print()

    print("Configuration")

    print(api_information())

    print()

    close()



