from pydantic import BaseModel

class CarFeatures(BaseModel):
    company: str
    year: int
    kms_driven: int
    fuel_type: str
    model: str