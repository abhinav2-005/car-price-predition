from pydantic import BaseModel,Field
from enum import Enum

class Transmission(str, Enum):
    manual = "Manual"
    automatic = "Automatic"
    semi_auto = "Semi-Auto"

class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    hybrid = "Hybrid"
    electric = "Electric"
    other = "Other"

class Valiadations(BaseModel):

    year : int = Field(...,example=2005)

    transmission : str = Field(...,example="Automatic")

    mileage : int = Field(...,example = 1234)

    tax : int = Field(...,example=1234)

    mpg : float = Field(...,example=57.7)

    engineSize : float = Field(...,example=1.0)

    model : str = Field(...,example= "Fiesta")

    transmission : Transmission

    fuelType : FuelType
