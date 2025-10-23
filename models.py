
from pydantic import BaseModel 


class product(BaseModel):
    id: int
    name: str 
    descriptiom: str 
    price: float 
    quantity: int 

  