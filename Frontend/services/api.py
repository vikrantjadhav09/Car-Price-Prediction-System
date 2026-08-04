"""
=========================================================
API Service Layer
AI Powered Car Price Prediction System
---------------------------------------------------------
Handles all communication between Streamlit and FastAPI.

Works in:

1. Local Development
   http://127.0.0.1:8000

2. Docker
   http://backend:8000

The backend URL is automatically selected using
the BACKEND_URL environment variable.
=========================================================
"""

from __future__ import annotations

import logging
import os
from typing import Any

import requests


# =========================================================
# CONFIGURATION
# =========================================================

DEFAULT_BACKEND_URL = "http://127.0.0.1:8000"

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    DEFAULT_BACKEND_URL
).rstrip("/")

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
    Centralized client for communicating with FastAPI.
    """

    def __init__(
        self,
        base_url: str = BACKEND_URL,
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

        logger.info(
            f"API Client initialized → {self.base_url}"
        )

    # =====================================================
    # URL BUILDER
    # =====================================================

    def url(self, endpoint: str) -> str:
        """
        Build complete API URL.

        Example:

        endpoint = "/predict"

        result:

        http://backend:8000/predict
        """

        endpoint = endpoint.lstrip("/")

        return f"{self.base_url}/{endpoint}"

    # =====================================================
    # GET REQUEST
    # =====================================================

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        try:

            response = self.session.get(
                self.url(endpoint),
                params=params,
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(
                f"GET {endpoint} failed: {e}"
            )

            return {
                "success": False,
                "message": str(e),
            }

        except ValueError as e:

            logger.error(
                f"Invalid JSON response from {endpoint}: {e}"
            )

            return {
                "success": False,
                "message": "Invalid response received from backend.",
            }

    # =====================================================
    # POST REQUEST
    # =====================================================

    def post(
        self,
        endpoint: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        try:

            logger.info(
                f"POST {endpoint}"
            )

            logger.debug(
                f"Payload: {payload}"
            )

            response = self.session.post(
                self.url(endpoint),
                json=payload,
                timeout=self.timeout,
            )

            response.raise_for_status()

            result = response.json()

            logger.info(
                f"POST {endpoint} → {response.status_code}"
            )

            return result

        except requests.exceptions.RequestException as e:

            logger.error(
                f"POST {endpoint} failed: {e}"
            )

            return {
                "success": False,
                "message": str(e),
            }

        except ValueError:

            logger.error(
                f"Invalid JSON response from {endpoint}"
            )

            return {
                "success": False,
                "message": "Invalid response received from backend.",
            }

    # =====================================================
    # DELETE REQUEST
    # =====================================================

    def delete(
        self,
        endpoint: str,
    ) -> dict[str, Any]:

        try:

            response = self.session.delete(
                self.url(endpoint),
                timeout=self.timeout,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            logger.error(
                f"DELETE {endpoint} failed: {e}"
            )

            return {
                "success": False,
                "message": str(e),
            }

        except ValueError:

            return {
                "success": False,
                "message": "Invalid response received from backend.",
            }

    # =====================================================
    # ROOT
    # =====================================================

    def root(self) -> dict[str, Any]:
        """
        Check FastAPI root endpoint.
        """

        return self.get("/")

    # =====================================================
    # PING
    # =====================================================

    def ping(self) -> bool:
        """
        Check whether backend is online.
        """

        try:

            response = self.session.get(
                self.url("/"),
                timeout=5,
            )

            return response.status_code == 200

        except requests.exceptions.RequestException:

            return False

    # =====================================================
    # HEALTH
    # =====================================================

    def health(self) -> dict[str, Any]:
        """
        Backend health check.
        """

        return self.get("/health")

    # =====================================================
    # VERSION
    # =====================================================

    def version(self) -> dict[str, Any]:
        """
        Get backend version.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get("/version")

    # =====================================================
    # MODEL INFO
    # =====================================================

    def model_info(self) -> dict[str, Any]:
        """
        Get ML model information.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get("/model/info")

    # =====================================================
    # PREDICTION
    # =====================================================

    def predict(
        self,
        features: dict[str, Any],
    ) -> dict[str, Any]:
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
            features,
        )

    # =====================================================
    # BATCH PREDICTION
    # =====================================================

    def batch_predict(
        self,
        records: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Predict prices for multiple vehicles.

        Note:
        This endpoint must exist in FastAPI.
        """

        payload = {
            "records": records
        }

        return self.post(
            "/predict/batch",
            payload,
        )

    # =====================================================
    # DATASET INFORMATION
    # =====================================================

    def dataset_info(self) -> dict[str, Any]:
        """
        Get dataset statistics.

        Note:
        This endpoint must exist in FastAPI.
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
    ) -> dict[str, Any]:
        """
        Get sample rows from dataset.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            "/dataset/sample",
            {
                "rows": rows
            },
        )

    # =====================================================
    # COMPANIES
    # =====================================================

    def companies(self) -> dict[str, Any]:
        """
        Get available car companies.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            "/companies"
        )

    # =====================================================
    # MODELS
    # =====================================================

    def models(
        self,
        company: str,
    ) -> dict[str, Any]:
        """
        Get available models for a company.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            "/models",
            {
                "company": company
            },
        )

    # =====================================================
    # FUEL TYPES
    # =====================================================

    def fuel_types(self) -> dict[str, Any]:
        """
        Get available fuel types.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            "/fuel-types"
        )

    # =====================================================
    # YEARS
    # =====================================================

    def years(self) -> dict[str, Any]:
        """
        Get available manufacturing years.

        Note:
        This endpoint must exist in FastAPI.
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
    ) -> dict[str, Any]:
        """
        Get prediction history.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            "/history",
            {
                "limit": limit
            },
        )

    # =====================================================
    # SINGLE HISTORY RECORD
    # =====================================================

    def history_by_id(
        self,
        prediction_id: int,
    ) -> dict[str, Any]:
        """
        Get a single prediction history record.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.get(
            f"/history/{prediction_id}"
        )

    # =====================================================
    # DELETE HISTORY RECORD
    # =====================================================

    def delete_prediction(
        self,
        prediction_id: int,
    ) -> dict[str, Any]:
        """
        Delete one prediction history record.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.delete(
            f"/history/{prediction_id}"
        )

    # =====================================================
    # CLEAR HISTORY
    # =====================================================

    def clear_history(self) -> dict[str, Any]:
        """
        Delete all prediction history.

        Note:
        This endpoint must exist in FastAPI.
        """

        return self.delete(
            "/history"
        )

    # =====================================================
    # CLOSE SESSION
    # =====================================================

    def close(self):
        """
        Close HTTP session.
        """

        try:

            self.session.close()

            logger.info(
                "API session closed."
            )

        except Exception as e:

            logger.error(
                f"Error closing API session: {e}"
            )


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================

class APIError(Exception):
    """
    Base API exception.
    """

    pass


class ConnectionError(APIError):
    """
    Backend connection error.
    """

    pass


class PredictionError(APIError):
    """
    Prediction error.
    """

    pass


# =========================================================
# RESPONSE HELPERS
# =========================================================

def is_success(
    response: dict[str, Any],
) -> bool:
    """
    Check whether API response was successful.
    """

    if not isinstance(response, dict):

        return False

    return response.get(
        "success",
        False
    )


def get_message(
    response: dict[str, Any],
) -> str:
    """
    Extract message from API response.
    """

    if not isinstance(response, dict):

        return "Invalid response."

    return response.get(
        "message",
        ""
    )


def get_data(
    response: dict[str, Any],
):
    """
    Extract data from API response.

    Supports both:

    {
        "data": {...}
    }

    and direct API responses.
    """

    if not isinstance(response, dict):

        return None

    return response.get(
        "data"
    )


# =========================================================
# BACKEND STATUS
# =========================================================

def is_backend_online() -> bool:
    """
    Check whether FastAPI backend is available.
    """

    return api.ping()


# =========================================================
# API INFORMATION
# =========================================================

def api_information() -> dict[str, Any]:
    """
    Return current API configuration.
    """

    return {
        "base_url": api.base_url,
        "timeout": api.timeout,
        "headers": dict(
            api.session.headers
        ),
    }


# =========================================================
# CHANGE BASE URL
# =========================================================

def set_base_url(
    host: str,
    port: int = 8000,
):
    """
    Dynamically change backend URL.

    Example:

    set_base_url(
        "127.0.0.1",
        8000
    )

    or

    set_base_url(
        "backend",
        8000
    )
    """

    global api

    new_url = f"http://{host}:{port}"

    api.close()

    api = APIClient(
        base_url=new_url,
        timeout=TIMEOUT,
    )

    logger.info(
        f"API Base URL updated → {api.base_url}"
    )


# =========================================================
# SINGLETON API INSTANCE
# =========================================================

api = APIClient()


# =========================================================
# STARTUP INFORMATION
# =========================================================

logger.info(
    "=================================================="
)

logger.info(
    "AI Powered Car Price Prediction API Client"
)

logger.info(
    f"Backend URL → {api.base_url}"
)

logger.info(
    f"Timeout → {api.timeout}s"
)

logger.info(
    "=================================================="
)


# =========================================================
# SELF TEST
# =========================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "AI Powered Car Price Prediction"
    )

    print("=" * 60)

    print()

    print(
        "Backend URL :",
        api.base_url
    )

    print(
        "Backend Online :",
        api.ping()
    )

    print()

    print(
        "Root Response :"
    )

    print(
        api.root()
    )

    print()

    print(
        "API Information :"
    )

    print(
        api_information()
    )

    print()

    api.close()